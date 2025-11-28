from fastapi import Request 
from fastapi import APIRouter
from fastapi.responses import JSONResponse 
from indexing.application.indexing import IndexingApplication, IndexingApplicationInput
from base import BaseModel
from logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/v1")

class IndexingRequest(BaseModel):
    course_code: str

@router.post("/indexing")
async def indexing(request: Request, indexing_request: IndexingRequest):
    indexing_app = IndexingApplication(request=request)
    result = await indexing_app.run(IndexingApplicationInput(
        course_code=indexing_request.course_code,
    ))
    return JSONResponse(content={
        'status': 'Indexing completed',
        'course_code': indexing_request.course_code,
    })
