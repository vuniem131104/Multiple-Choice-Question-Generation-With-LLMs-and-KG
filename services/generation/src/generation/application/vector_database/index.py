from generation.domain.vector_db_construction import VectorDatabaseInput
from generation.domain.vector_db_construction import VectorDatabaseService 
from base import BaseModel 
from base import BaseApplication
from fastapi import Request

class VectorDatabaseIndexApplicationInput(BaseModel):
    course_code: str 
    
class VectorDatabaseIndexApplicationOutput(BaseModel):
    course_code: str 
    

class VectorDatabaseIndexApplication(BaseApplication):
    request: Request
    
    async def run(self, inputs: VectorDatabaseIndexApplicationInput) -> VectorDatabaseIndexApplicationOutput:
        service = VectorDatabaseService(
            litellm_service=self.request.app.state.litellm_service,
            settings=self.request.app.state.settings.vector_database,
            client=self.request.app.state.chroma_db 
        )
        
        outputs = await service.process(
            inputs=VectorDatabaseInput(
                course_code=inputs.course_code
            )
        )
        
        return VectorDatabaseIndexApplicationOutput(
            course_code=inputs.course_code
        )