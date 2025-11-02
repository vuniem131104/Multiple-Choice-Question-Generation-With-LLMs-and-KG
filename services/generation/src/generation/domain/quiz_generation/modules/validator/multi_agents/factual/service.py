from generation.domain.quiz_generation.prompts import FACTUAL_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import FACTUAL_USER_PROMPT
from generation.shared.states import ValidatorState
from generation.shared.settings import FactualSetting
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

class FactualMessage(BaseModel):
    factual_message: str = Field(..., description="The factual accuracy feedback message")
    factual_score: int = Field(..., description="The factual accuracy score (0-100)")


class FactualService(BaseService):
    settings: FactualSetting
    litellm_service: LiteLLMService

    async def process(self, state: ValidatorState) -> dict[str, Any]:
        try:
            question = state['quiz_question']
            distractors_text = "\n".join([f"- {distractor}" for distractor in question.distractors])
            user_content = FACTUAL_USER_PROMPT.format(
                question=question.question,
                correct_answer=question.answer,
                distractors=distractors_text,
                topic_name=question.topic.name,
                topic_description=question.topic.description,
                difficulty_level=question.topic.difficulty_level,
            )
            
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=FACTUAL_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=user_content
                        )
                    ],
                    response_format=FactualMessage,
                    temperature=self.settings.temperature, 
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            return {
                "factual_message": output.response.factual_message,
                "factual_score": output.response.factual_score
            }
        except Exception as e:
            logger.exception(
                "Error when processing factual validation with litellm",
                extra={
                    "error": str(e),
                } 
            )
            raise e

