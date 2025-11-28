from __future__ import annotations


DELETE_ENTITY_DESCRIPTION_QUERY = """
MATCH (d:Description)
WHERE d.uid IN $description_uids
OPTIONAL MATCH (d)-[:DESCRIBED]-(e:Entity)

WITH collect(d) as descriptions

FOREACH (d IN descriptions | DETACH DELETE d)
RETURN $cluster_id as cluster_id, size(descriptions) as deleted_count
"""


MERGE_ENTITY_DESCRIPTION_QUERY = """
MATCH (d:Description)
WHERE d.uid IN $description_uids
OPTIONAL MATCH (d)-[:DESCRIBED]-(e:Entity)

WITH collect(d) as descriptions,
     collect(d.chunk_uid) as description_chunk_uids,
     collect(DISTINCT e) as entities

CREATE (new_desc:Description {
    uid: $uid,
    text: $text,
    type: 'ENTITY',
    embedding: $embedding,
    chunk_uid: apoc.text.join(description_chunk_uids, '|')
})

WITH new_desc, entities, descriptions

UNWIND entities AS e
CREATE (e)-[:DESCRIBED]->(new_desc)

RETURN $cluster_id as cluster_id,
       size(descriptions) as merged_count
"""


CREATE_ENTITY_TYPE_INDEX_QUERY = 'CREATE INDEX $entity_type_index IF NOT EXISTS FOR (e:Entity) ON (e.type)'


GET_ENTITY_TYPE_QUERY = """MATCH (e:Entity)-[:DESCRIBED]->(d:Description)
USING INDEX e:Entity(type)
WHERE e.type = $type AND d.embedding IS NOT NULL AND size(d.embedding) > 0
RETURN d
"""

GET_ALL_ENTITY_TYPES_QUERY = 'MATCH (e:Entity) RETURN collect(DISTINCT e.type) as types'
