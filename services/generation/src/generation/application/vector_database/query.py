from generation.domain.vector_db_construction import VectorDatabaseInput
from generation.domain.vector_db_construction import VectorDatabaseService 
from base import BaseModel 
from base import BaseApplication
from fastapi import Request
from typing import Any
from typing import Optional

class VectorDatabaseQueryApplicationInput(BaseModel):
    course_code: str 
    query: str
    
class VectorDatabaseQueryApplicationOutput(BaseModel):
    course_code: str 
    results: dict[str, Any]
    

class VectorDatabaseQueryApplication(BaseApplication):
    request: Request
    
    async def run(self, inputs: VectorDatabaseQueryApplicationInput) -> VectorDatabaseQueryApplicationOutput:
        service = VectorDatabaseService(
            litellm_service=self.request.app.state.litellm_service,
            settings=self.request.app.state.settings.vector_database,
            client=self.request.app.state.chroma_db 
        )
        
        outputs = await service.query(
            course_code=inputs.course_code,
            topic_name=inputs.query
        )
        
        return VectorDatabaseQueryApplicationOutput(
            course_code=inputs.course_code,
            results=outputs
        )