from generation.shared.models import Topic
from generation.domain.quiz_generation.prompts import EXPLANATION_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import EXPLANATION_USER_PROMPT
from generation.shared.settings import ExplanationGeneratorSetting
from generation.domain.quiz_generation.modules.question_answer_generator.service import QuestionAnswer

from pydantic import Field

from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import CompletionMessage
from lite_llm import Role
from logger import get_logger


logger = get_logger(__name__)


class ExplanationGeneratorInput(BaseModel):
    question_answer: QuestionAnswer
    distractors: list[str]
    topic: Topic
    week_number: int
    course_code: str
    

class ExplanationGeneratorOutput(BaseModel):
    explanation: str
    week_number: int
    course_code: str
    

class ExplanationGeneratorService(BaseService):
    settings: ExplanationGeneratorSetting
    litellm_service: LiteLLMService

    async def process(self, inputs: ExplanationGeneratorInput) -> ExplanationGeneratorOutput:
        try:
            distractors_list = "\n".join([f"- {distractor}" for distractor in inputs.distractors])
            
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=EXPLANATION_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=EXPLANATION_USER_PROMPT.format(
                                question=inputs.question_answer.question,
                                answer=inputs.question_answer.answer,
                                distractors_list=distractors_list,
                                topic_name=inputs.topic.name,
                                topic_description=inputs.topic.description,
                                difficulty_level=inputs.topic.difficulty_level,
                                bloom_taxonomy_level=inputs.topic.bloom_taxonomy_level,
                                estimated_right_answer_rate=inputs.topic.estimated_right_answer_rate,
                                week_number=inputs.week_number,
                                course_code=inputs.course_code
                            )
                        )
                    ],
                    temperature=self.settings.temperature,
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            return ExplanationGeneratorOutput(
                explanation=output.response,
                week_number=inputs.week_number,
                course_code=inputs.course_code
            )
        except Exception as e:
            logger.exception(
                "Error when processing explanation generation with litellm",
                extra={
                    "week_number": inputs.week_number,
                    "course_code": inputs.course_code,
                    "topic_name": inputs.topic.name,
                    "question": inputs.question_answer.question,
                    "answer": inputs.question_answer.answer,
                    "distractors": inputs.distractors,
                    "error": str(e),
                } 
            )
            raise e

