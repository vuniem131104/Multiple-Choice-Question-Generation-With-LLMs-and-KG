from __future__ import annotations

from uuid import uuid4

import numpy as np
import pandas as pd
from indexing.shared.settings.deduplicate import DeduplicateSetting
from lite_llm import CompletionMessage
from lite_llm import LiteLLMEmbeddingInput
from lite_llm import LiteLLMInput
from lite_llm import LiteLLMService
from lite_llm import Role
from logger import get_logger
from graph_db import Neo4jService

from indexing.domain.deduplicate.cypher import CREATE_ENTITY_TYPE_INDEX_QUERY
from indexing.domain.deduplicate.cypher import DELETE_ENTITY_DESCRIPTION_QUERY
from indexing.domain.deduplicate.cypher import GET_ALL_ENTITY_TYPES_QUERY
from indexing.domain.deduplicate.cypher import GET_ENTITY_TYPE_QUERY
from indexing.domain.deduplicate.cypher import MERGE_ENTITY_DESCRIPTION_QUERY
from indexing.domain.deduplicate.models import ClusterInfo
from indexing.domain.deduplicate.models import ClusterInfos
from indexing.domain.deduplicate.models import DescriptionInfo
from indexing.domain.deduplicate.prompts import SYSTEM_PROMPT
from indexing.domain.deduplicate.utils import calculate_cosine_similarity_matrix
from base import BaseModel
from base import BaseService

logger = get_logger(__name__)


class DeDuplicateInput(BaseModel):
    types: list[str]


class DeDuplicateOutput(BaseModel):
    pass


class DeDuplicateService(BaseService):

    litellm_service: LiteLLMService
    neo4j_service: Neo4jService
    settings: DeduplicateSetting

    async def get_all_entity_types(self) -> list[str]:
        """Get all entity types from the database.

        Returns:
            list[str]: A list of all entity types.
        """
        result = await self.neo4j_service.execute_query(
            cypher=GET_ALL_ENTITY_TYPES_QUERY,
            output_format='pandas',
        )

        return result.to_dict(orient='records')[0]['types']

    def get_entity_pairs(
        self,
        cosine_similarity_matrix: np.ndarray,
        data: list[DescriptionInfo],
    ) -> list[tuple[DescriptionInfo, DescriptionInfo]]:
        """Get entity pairs from the cosine similarity matrix.

        Args:
            cosine_similarity_matrix (np.ndarray): The cosine similarity matrix.
            data (list[DescriptionInfo]): The list of DescriptionInfo objects.

        Returns:
            list[tuple[DescriptionInfo, DescriptionInfo]]: A list of tuples representing the pairs of entities.
        """
        entity_pairs: list[tuple[DescriptionInfo, DescriptionInfo]] = []
        for i in range(len(cosine_similarity_matrix)):
            for j in range(i + 1, len(cosine_similarity_matrix[i])):
                if cosine_similarity_matrix[i][j] >= self.settings.threshold:
                    entity_pairs.append((data[i], data[j]))
        return entity_pairs

    async def get_clusters(self, type: str, cosine_similarity_matrix: np.ndarray, data: list[DescriptionInfo]) -> ClusterInfos:
        """Get clusters from the cosine similarity matrix.

        Args:
            cosine_similarity_matrix (np.ndarray): The cosine similarity matrix.
            data (list[DescriptionInfo]): The list of DescriptionInfo objects.

        Returns:
            ClusterInfos: A ClusterInfos object containing the clusters formed from the data.
        """

        parent = list(range(len(data)))

        list_cluster_info: list = []

        clusters: dict = {}

        entity_pairs = self.get_entity_pairs(cosine_similarity_matrix, data)

        def __find(x):
            """Find the root representative of the set containing x.

            Args:
                x (int): The index of the element to find.

            Returns:
                int: The root representative of the set.
            """
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def __union(x, y):
            """Union the sets containing x and y.

            Args:
                x (int): The index of the first element.
                y (int): The index of the second element.
            """
            px = __find(x)
            py = __find(y)
            if px != py:
                parent[py] = px

        for pair in entity_pairs:
            idx1 = data.index(pair[0])
            idx2 = data.index(pair[1])
            __union(idx1, idx2)

        for idx in range(len(data)):
            root = __find(idx)
            clusters.setdefault(root, []).append(data[idx])

        for members in clusters.values():

            if len(members) <= 1:
                continue

            llm_response = await self.litellm_service.process_async(
                LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=SYSTEM_PROMPT,
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content='\n'.join(member.text for member in members),
                        ),
                    ],
                ),
            )

            deduplicated_embedding = self.litellm_service.embedding_ollama(
                LiteLLMEmbeddingInput(
                    text=str(llm_response.response)
                ),
            )

            list_cluster_info.append(
                ClusterInfo(
                    description_ids=[member.uid for member in members],
                    description_text=[member.text for member in members],
                    text=str(llm_response.response),
                    embedding=deduplicated_embedding.embedding,
                ),
            )

        return ClusterInfos(
            clusters=list_cluster_info,
            type=type,
        )

    async def merge_entity_description_nodes(
        self,
        cluster_infos: ClusterInfos,
    ) -> pd.DataFrame:
        """
        Merge entity description nodes into a DataFrame.

        Args:
            cluster_infos (ClusterInfos): The cluster information containing description nodes to delete.

        Returns:
            pd.DataFrame: A DataFrame containing the merged entity descriptions.
        """

        results: list = []
        try:
            logger.info(
                'Processing merge clusters',
                extra={
                    'type': cluster_infos.type,
                    'num_clusters': len(cluster_infos.clusters),
                },
            )
            for cluster_id, cluster in enumerate(cluster_infos.clusters, start=1):
                description_uids = cluster.description_ids

                if not description_uids or len(description_uids) == 1:
                    logger.warning(
                        f'Skipping merge for cluster {cluster_id} with insufficient description nodes',
                    )
                    continue

                result = await self.neo4j_service.execute_query(
                    cypher=MERGE_ENTITY_DESCRIPTION_QUERY,
                    parameters={
                        'cluster_id': cluster_id,
                        'description_uids': description_uids,
                        'uid': str(uuid4()),
                        'text': cluster.text,
                        'embedding': cluster.embedding,
                    },
                    output_format='pandas',
                )

                if not isinstance(result, pd.DataFrame):
                    raise Exception(
                        f'Invalid output format, expected dataframe, got {type(result)}',
                    )

                results.append(result)

            return pd.concat(results, ignore_index=True) if results else pd.DataFrame()
        except Exception as e:
            logger.exception(
                'Error while merging description nodes',
                extra={
                    'error': str(e),
                },
            )
            raise e

    async def delete_entity_description_nodes(
        self,
        cluster_infos: ClusterInfos,
    ) -> pd.DataFrame:
        """Delete description nodes from the database.

        Args:
            cluster_infos (ClusterInfos): The cluster information containing description nodes to delete.

        Returns:
            pd.DataFrame: A DataFrame containing the results of the delete operations.
        """
        results: list = []
        try:
            logger.info(
                'Processing delete clusters',
                extra={
                    'type': cluster_infos.type,
                    'num_clusters': len(cluster_infos.clusters),
                },
            )
            for cluster_id, cluster_info in enumerate(cluster_infos.clusters, start=1):
                description_uids = cluster_info.description_ids

                if not description_uids or len(description_uids) == 1:
                    logger.warning(
                        f'Skipping delete for cluster {cluster_id} with insufficient description nodes',
                    )
                    continue

                result = await self.neo4j_service.execute_query(
                    cypher=DELETE_ENTITY_DESCRIPTION_QUERY,
                    parameters={
                        'description_uids': description_uids,
                        'cluster_id': cluster_id,
                    },
                    output_format='pandas',
                )

                if not isinstance(result, pd.DataFrame):
                    logger.warning(
                        'Invalid output format, expected dataframe',
                        extra={
                            'type': type(result),
                            'description_uids': description_uids,
                            'cluster_id': cluster_id,
                        },
                    )
                    raise Exception(
                        f'Invalid output format, expected dataframe, got {type(result)}',
                    )

                results.append(result)

            return pd.concat(results, ignore_index=True) if results else pd.DataFrame()
        except Exception as e:
            logger.exception(
                'Error while deleting description nodes',
                extra={
                    'error': str(e),
                },
            )
            raise e

    async def process(
        self,
        inputs: DeDuplicateInput,
    ) -> DeDuplicateOutput:
        """Process de-duplication of entity descriptions.

        Args:
            inputs (DeDuplicateInput): The input data for de-duplication.

        Returns:
            DeDuplicateOutput: The output data after de-duplication.
        """

        _ = await self.neo4j_service.execute_query(
            cypher=CREATE_ENTITY_TYPE_INDEX_QUERY,
            parameters={
                'entity_type_index': 'entity_description_index',
            },
            output_format='pandas',
        )

        for type in inputs.types:
            logger.info(f'Processing type: {type}')
            result = await self.neo4j_service.execute_query(
                cypher=GET_ENTITY_TYPE_QUERY,
                parameters={
                    'type': type,
                },
                output_format='pandas',
            )
            
            description_list = result.to_dict(orient='records')
            description_list_ = [desc['d'] for desc in description_list if 'd' in desc]

            if not description_list_:
                logger.warning('No descriptions found for type', extra={'type': type})
                continue

            description_list_object = [
                DescriptionInfo(
                    uid=desc['uid'],
                    text=desc['text'],
                    type="ENTITY",
                    embedding=desc['embedding'],
                )
                for desc in description_list_
            ]

            cosine_similarity_matrix = calculate_cosine_similarity_matrix(np.vstack([d.embedding for d in description_list_object]))
            clusters = await self.get_clusters(type, cosine_similarity_matrix, description_list_object)

            _ = await self.merge_entity_description_nodes(clusters)
            _ = await self.delete_entity_description_nodes(clusters)

        return DeDuplicateOutput()
    
async def main():

    from graph_db import Neo4jService, Neo4jSetting
    from lite_llm import LiteLLMEmbeddingInput, LiteLLMService, LiteLLMSetting
    from pydantic import HttpUrl, SecretStr

    litellm_setting=LiteLLMSetting(
        url=HttpUrl("http://localhost:9510"),
        token=SecretStr("abc123"),
        model="gemini-2.5-flash",
        frequency_penalty=0.0,
        n=1,
        temperature=0.0,
        top_p=1.0,
        max_completion_tokens=10000,
        dimension=1024,
        embedding_model="qwen3-embedding:0.6b"
    )

    litellm_service = LiteLLMService(litellm_setting=litellm_setting)

    neo4j_service = Neo4jService(
        settings=Neo4jSetting(
            uri="bolt://localhost:17687",
            username="neo4j",
            password="4_Kz1pLYqtmVsxFJED_gxTN8rBcu4oQKAEqw9mm6zUHY"
        )
    )
    deduplicate_service = DeDuplicateService(
        neo4j_service=neo4j_service,
        litellm_service=litellm_service,
        settings=DeduplicateSetting(
            threshold=0.85,
        ),
    )
    _ = await deduplicate_service.process(
        DeDuplicateInput(
            types=["equation", "formula", "framework", "function", "loss_function", "method", "metric", "model", "operation", "optimizer", "parameter", "policy", "problem", "process", "property", "research_area", "technique", "tool", "type"],
        ),
    )
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())