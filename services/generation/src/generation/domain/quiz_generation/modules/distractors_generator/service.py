from generation.domain.quiz_generation.modules.question_answer_generator.service import QuestionAnswer
from generation.domain.quiz_generation.prompts import DISTRACTORS_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import DISTRACTORS_USER_PROMPT
from generation.shared.settings import DistractorsGeneratorSetting
from generation.shared.models import Topic

from pydantic import Field

from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import CompletionMessage
from lite_llm import Role
from logger import get_logger


logger = get_logger(__name__)

class Distractors(BaseModel):
    distractors: list[str] = Field(..., description="List of generated distractors for the question")


class DistractorsGeneratorInput(BaseModel):
    question_answer: QuestionAnswer
    common_mistakes: list[str]
    topic: Topic
    week_number: int
    course_code: str
    
    
class DistractorsGeneratorOutput(BaseModel):
    distractors: list[str]
    week_number: int
    course_code: str
    
class DistractorsGeneratorService(BaseService):
    settings: DistractorsGeneratorSetting
    litellm_service: LiteLLMService

    async def process(self, inputs: DistractorsGeneratorInput) -> DistractorsGeneratorOutput:
        try:
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=DISTRACTORS_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=DISTRACTORS_USER_PROMPT.format(
                                question=inputs.question_answer.question,
                                answer=inputs.question_answer.answer,
                                topic_name=inputs.topic.name,
                                topic_description=inputs.topic.description,
                                difficulty_level=inputs.topic.difficulty_level,
                                bloom_taxonomy_level=inputs.topic.bloom_taxonomy_level,
                                estimated_right_answer_rate=inputs.topic.estimated_right_answer_rate,
                                week_number=inputs.week_number,
                                course_code=inputs.course_code,
                                common_mistakes=', '.join(inputs.common_mistakes)
                            )
                        )
                    ],
                    response_format=Distractors,
                    temperature=self.settings.temperature,
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            
            return DistractorsGeneratorOutput(
                distractors=output.response.distractors[:3],
                week_number=inputs.week_number,
                course_code=inputs.course_code
            )
        except Exception as e:
            logger.exception(
                "Error when processing distractor generation with litellm",
                extra={
                    "week_number": inputs.week_number,
                    "course_code": inputs.course_code,
                    "topic_name": inputs.topic.name,
                    "question": inputs.question_answer.question,
                    "answer": inputs.question_answer.answer,
                    "error": str(e),
                } 
            )
            raise e
