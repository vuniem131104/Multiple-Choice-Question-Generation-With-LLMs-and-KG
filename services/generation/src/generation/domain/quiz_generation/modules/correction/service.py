from generation.domain.quiz_generation.prompts import QUIZ_CORRECTION_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import QUIZ_CORRECTION_USER_PROMPT
from generation.shared.models import QuizQuestion
from generation.shared.settings import QuizCorrectionSetting

from pydantic import Field

from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import CompletionMessage
from lite_llm import Role
from logger import get_logger


logger = get_logger(__name__)

class QuizQuestionResponse(BaseModel):
    question: str = Field(..., description="The quiz question text")
    answer: str = Field(..., description="The correct answer text")
    distractors: list[str] = Field(..., description="List of incorrect answer options")
    explanation: str = Field(..., description="Explanation for the correct answer and distractors")


class QuizCorrectionInput(BaseModel):
    validator_feedback: str
    question_metadata: QuizQuestion
    

class QuizCorrectionOutput(BaseModel):
    corrected_question: QuizQuestion
    

class QuizCorrectionService(BaseService):
    settings: QuizCorrectionSetting
    litellm_service: LiteLLMService

    async def process(self, inputs: QuizCorrectionInput) -> QuizCorrectionOutput:
        try:

            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=QUIZ_CORRECTION_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=QUIZ_CORRECTION_USER_PROMPT.format(
                                original_question=inputs.question_metadata.question,
                                original_answer=inputs.question_metadata.answer,
                                original_distractors_list="\n".join([f"- {distractor}" for distractor in inputs.question_metadata.distractors]),
                                original_explanation=inputs.question_metadata.explanation,
                                validator_feedback=inputs.validator_feedback,
                                topic_name=inputs.question_metadata.topic.name,
                                topic_description=inputs.question_metadata.topic.description,
                                difficulty_level=inputs.question_metadata.topic.difficulty_level,
                                bloom_taxonomy_level=inputs.question_metadata.topic.bloom_taxonomy_level,
                                course_code=inputs.question_metadata.course_code
                            )
                        )
                    ],
                    response_format=QuizQuestionResponse,
                    temperature=self.settings.temperature,
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            return QuizCorrectionOutput(
                corrected_question=QuizQuestion(
                    question=output.response.question,
                    answer=output.response.answer,
                    distractors=output.response.distractors,
                    explanation=output.response.explanation,
                    topic=inputs.question_metadata.topic,
                    course_code=inputs.question_metadata.course_code,
                    week_number=inputs.question_metadata.week_number
                )
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
            return QuizCorrectionOutput(
                corrected_question=inputs.question_metadata
            )