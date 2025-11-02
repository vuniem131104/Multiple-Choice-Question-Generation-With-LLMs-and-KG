from base import BaseModel
from base import BaseService 
from lite_llm import LiteLLMEmbeddingInput 
from lite_llm import LiteLLMService
import chromadb
import json 
from uuid import uuid4 
from typing import Any
from tqdm import tqdm
import asyncio
from generation.shared.settings import VectorDatabaseSetting


class VectorDatabaseInput(BaseModel):
    course_code: str 
    
class VectorDatabaseOutput(BaseModel):
    course_code: str 
    
class VectorDatabaseService(BaseService):
    litellm_service: LiteLLMService
    settings: VectorDatabaseSetting
    client: chromadb.ClientAPI
    
    async def process(self, inputs: VectorDatabaseInput) -> VectorDatabaseOutput:
        collection = self.client.get_or_create_collection(name="questions")
        
        with open(f"/home/lehoangvu/KLTN/services/generation/src/generation/shared/static_files/{inputs.course_code}/mcqs.json", "r") as f:
            data = json.load(f)
            
        for item in tqdm(data):
            embedding = await self.litellm_service.embedding_llm_async(
                inputs=LiteLLMEmbeddingInput(
                    text=item['question']
                )
            )
            options = [
                f"{key}. {value}"
                for key, value in item['options'].items()
            ]
            collection.add(
                ids=[str(uuid4())],
                embeddings=[embedding.embedding],
                documents=[item['question']],
                metadatas=[{
                    "options": "\n".join(options),
                    "answer": item['answer'],
                    "explanation": item['explanation'],
                    "course_code": inputs.course_code
                }]
            )
            await asyncio.sleep(1)
            
        return VectorDatabaseOutput(
            course_code=inputs.course_code,
        )
            
    async def query(self, course_code: str, topic_name: str, top_k: int = 3) -> dict[str, Any]:
        collection = self.client.get_or_create_collection(name="questions")
        embeddings = await self.litellm_service.embedding_llm_async(
                inputs=LiteLLMEmbeddingInput(
                    text=topic_name
                )
        )
        results = collection.query(
            query_embeddings=[embeddings.embedding],
            n_results=top_k,
            where={"course_code": course_code}
        )
        
        return results
    