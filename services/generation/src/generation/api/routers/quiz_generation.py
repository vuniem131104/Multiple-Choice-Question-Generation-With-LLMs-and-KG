from fastapi import Request 
from fastapi import APIRouter
from fastapi.responses import JSONResponse 
from generation.application.quiz_generation import QuizApplication
from generation.application.quiz_generation import QuizApplicationInput
from base import BaseModel
from logger import get_logger
from generation.shared.models import QuizQuestion

logger = get_logger(__name__)
quiz_router = APIRouter(tags=["mcq"])

class QuizRequest(BaseModel):
    number_of_topics: int
    common_mistakes: list[str] = []
    course_code: str
    week_number: int

class QuizResponse(BaseModel):
    questions: list[QuizQuestion]
    course_code: str
    week_number: int

@quiz_router.post("/generate_quiz")
async def generate_quiz(request: Request, quiz_request: QuizRequest):
    quiz_application = QuizApplication(request=request)
    outputs = await quiz_application.run(
        inputs=QuizApplicationInput(
            course_code=quiz_request.course_code,
            week_number=quiz_request.week_number,
            number_of_topics=quiz_request.number_of_topics,
            common_mistakes=quiz_request.common_mistakes
        )
    )

    return JSONResponse(
        content={
            "questions": [question.model_dump() for question in outputs.questions],
            "course_code": outputs.course_code,
            "week_number": outputs.week_number
        }
    )
