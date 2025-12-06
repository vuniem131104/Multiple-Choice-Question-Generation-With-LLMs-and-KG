from base import BaseModel 
from base import BaseApplication 
from fastapi import Request
from generation.domain.quiz_generation import QuizGenerationService
from generation.domain.quiz_generation import QuizGenerationInput
from generation.shared.models import QuizQuestion
from logger import get_logger


logger = get_logger(__name__)

class QuizApplicationInput(BaseModel):
    number_of_topics: int
    common_mistakes: list[str] = []
    week_number: int
    course_code: str
    

class QuizApplicationOutput(BaseModel):
    questions: list[QuizQuestion]
    week_number: int
    course_code: str

class QuizApplication(BaseApplication):
    
    request: Request
    
    async def run(self, inputs: QuizApplicationInput) -> QuizApplicationOutput:
        quiz_generation_service = QuizGenerationService(
            settings=self.request.app.state.settings.quiz,
            litellm_service=self.request.app.state.litellm_service,
            minio_service=self.request.app.state.minio_service,
        )

        outputs = await quiz_generation_service.process(
            inputs=QuizGenerationInput(
                number_of_topics=inputs.number_of_topics,
                common_mistakes=inputs.common_mistakes,
                week_number=inputs.week_number,
                course_code=inputs.course_code
            )
        )
        
        return QuizApplicationOutput(
            questions=outputs.quiz_questions,
            week_number=outputs.week_number,
            course_code=outputs.course_code
        )