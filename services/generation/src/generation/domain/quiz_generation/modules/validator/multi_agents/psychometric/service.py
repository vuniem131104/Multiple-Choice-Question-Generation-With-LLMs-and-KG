from generation.domain.quiz_generation.prompts import PSYCHOMETRIC_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import PSYCHOMETRIC_USER_PROMPT
from generation.shared.states import ValidatorState
from generation.shared.settings import PsychometricSetting
from generation.shared.models import QuizQuestion
from typing import Any
from pydantic import Field

from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import CompletionMessage
from lite_llm import Role
from logger import get_logger

logger = get_logger(__name__)

class PsychometricMessage(BaseModel):
    psychometric_message: str = Field(..., description="The psychometric quality feedback message")
    psychometric_score: int = Field(..., description="The psychometric quality score (0-100)")


class PsychometricService(BaseService):
    settings: PsychometricSetting
    litellm_service: LiteLLMService

    async def process(self, state: ValidatorState) -> dict[str, Any]:
        try:
            question = state['quiz_question']
            distractors_text = "\n".join([f"- {distractor}" for distractor in question.distractors])
            user_content = PSYCHOMETRIC_USER_PROMPT.format(
                question=question.question,
                correct_answer=question.answer,
                distractors=distractors_text,
                topic_name=question.topic.name,
                topic_description=question.topic.description,
                difficulty_level=question.topic.difficulty_level,
                bloom_taxonomy_level=question.topic.bloom_taxonomy_level,
                estimated_right_answer_rate=question.topic.estimated_right_answer_rate * 100  # Convert to percentage
            )
            
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=PSYCHOMETRIC_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=user_content
                        )
                    ],
                    response_format=PsychometricMessage,
                    temperature=self.settings.temperature,
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            return {
                "psychometric_message": output.response.psychometric_message,
                "psychometric_score": output.response.psychometric_score
            }
        except Exception as e:
            logger.exception(
                "Error when processing psychometric validation with litellm",
                extra={
                    "error": str(e),
                } 
            )
            raise e

