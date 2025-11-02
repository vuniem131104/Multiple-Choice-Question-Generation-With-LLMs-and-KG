from fastapi import Request 
from fastapi import APIRouter
from fastapi.responses import JSONResponse 
from generation.application.vector_database import VectorDatabaseIndexApplication
from generation.application.vector_database import VectorDatabaseIndexApplicationInput
from generation.application.vector_database import VectorDatabaseQueryApplication
from generation.application.vector_database import VectorDatabaseQueryApplicationInput
from base import BaseModel
from logger import get_logger

logger = get_logger(__name__)
vector_database_router = APIRouter(tags=["vector_database"])

class VectorDatabaseIndexRequest(BaseModel):
    course_code: str 
    
class VectorDatabaseQueryRequest(BaseModel):
    course_code: str 
    query: str
    
@vector_database_router.post("/index")
async def index(request: Request, vector_database_index_request: VectorDatabaseIndexRequest):
    vector_database_index_application = VectorDatabaseIndexApplication(request=request)
    outputs = await vector_database_index_application.run(
        inputs=VectorDatabaseIndexApplicationInput(
            course_code=vector_database_index_request.course_code
        )
    )
    
    return JSONResponse(
        content={
            "course_code": outputs.course_code,
            "message": "Indexing successfully"
        }
    )
    
@vector_database_router.post("/query")
async def query(request: Request, vector_database_query_request: VectorDatabaseQueryRequest):
    vector_database_query_application = VectorDatabaseQueryApplication(request=request)
    outputs = await vector_database_query_application.run(
        inputs=VectorDatabaseQueryApplicationInput(
            course_code=vector_database_query_request.course_code,
            query=vector_database_query_request.query
        )
    )
    
    return JSONResponse(
        content={
            "results": outputs.results,
            "course_code": outputs.course_code
        }
    )
    