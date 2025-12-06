from __future__ import annotations

from pydantic import Field
from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import LiteLLMEmbeddingInput
from lite_llm import CompletionMessage
from lite_llm import Role
from generation.domain.quiz_generation.prompts import QUESTION_ANSWER_SYSTEM_PROMPT
from generation.domain.quiz_generation.prompts import QUESTION_ANSWER_USER_PROMPT
from generation.shared.models import Topic
from generation.shared.settings import QuestionAnswerGeneratorSetting
from logger import get_logger
import httpx
import json
from typing import Optional

logger = get_logger(__name__)

class QuestionAnswer(BaseModel):
    question: str = Field(..., description="The generated question")
    answer: str = Field(..., description="The generated answer")

class QuestionAnswerGeneratorInput(BaseModel):
    topic: Topic
    week_number: int
    course_code: str 

class QuestionAnswerGeneratorOutput(BaseModel):
    question_answer: QuestionAnswer
    week_number: int
    course_code: str
    rag_context: Optional[str] = None
    

class QuestionAnswerGeneratorService(BaseService):
    litellm_service: LiteLLMService
    settings: QuestionAnswerGeneratorSetting

    async def _get_rag_context(self, query: str) -> Optional[str]:
        """
        Gọi RAG API để lấy context liên quan đến query
        """
        try:
            rag_url = "http://rag:3011/v1/local_search"
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    rag_url,
                    headers={
                        "accept": "application/json",
                        "Content-Type": "application/json"
                    },
                    json={"query": query}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    context_parts = []
                    
                    if "chunk_df" in result and result["chunk_df"]:
                        for chunk_data in result["chunk_df"]:
                            if "chunk" in chunk_data:
                                context_parts.append(f"**Nội dung từ tài liệu:**\n{chunk_data['chunk']}")
                            
                            if "entities" in chunk_data and chunk_data["entities"]:
                                entities_text = "\n".join([f"- {entity}" for entity in chunk_data["entities"]])
                                context_parts.append(f"**Các khái niệm quan trọng:**\n{entities_text}")
                            
                            if "relationships" in chunk_data and chunk_data["relationships"]:
                                relationships_text = "\n".join([f"- {rel}" for rel in chunk_data["relationships"]])
                                context_parts.append(f"**Mối quan hệ:**\n{relationships_text}")
                    
                    if context_parts:
                        return "\n\n".join(context_parts)
                    else:
                        logger.warning(
                            "RAG API returned empty or invalid context",
                            extra={"query": query, "response": result}
                        )
                        return None
                        
                else:
                    logger.warning(
                        "RAG API call failed",
                        extra={"query": query, "status_code": response.status_code, "response": response.text}
                    )
                    return None
                    
        except Exception as e:
            logger.exception(
                "Error calling RAG API",
                extra={"query": query, "error": str(e)}
            )
            return None

    async def process(self, inputs: QuestionAnswerGeneratorInput, get_rag_context=True) -> QuestionAnswerGeneratorOutput:
        # Lấy RAG context
        rag_context = await self._get_rag_context(inputs.topic.description) if get_rag_context else None
        
        logger.info(
            "Retrieved similar questions from database",
            extra={
                "course_code": inputs.course_code,
                "week_number": inputs.week_number,
                "topic_name": inputs.topic.name,
                "rag_context_available": rag_context is not None
            }
        )
            
        try:
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    model=self.settings.model,
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=QUESTION_ANSWER_SYSTEM_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            content=QUESTION_ANSWER_USER_PROMPT.format(
                                topic_name=inputs.topic.name,
                                topic_description=inputs.topic.description,
                                difficulty_level=inputs.topic.difficulty_level,
                                bloom_taxonomy_level=inputs.topic.bloom_taxonomy_level,
                                estimated_right_answer_rate=inputs.topic.estimated_right_answer_rate,
                                context=rag_context if rag_context else "Không có thông tin bổ sung từ tài liệu."
                            )
                        )
                    ],
                    response_format=QuestionAnswer,
                    temperature=self.settings.temperature,
                    top_p=self.settings.top_p,
                    n=self.settings.n,
                    frequency_penalty=self.settings.frequency_penalty,
                    max_completion_tokens=self.settings.max_completion_tokens,
                    reasoning_effort=self.settings.reasoning_effort,
                )
            )
            
            logger.info(
                "Question-Answer generated successfully",
                extra={
                    "course_code": inputs.course_code,
                    "week_number": inputs.week_number,
                    "topic_name": inputs.topic.name,
                }
            )

            return QuestionAnswerGeneratorOutput(
                question_answer=output.response,
                week_number=inputs.week_number,
                course_code=inputs.course_code,
                rag_context=rag_context
            )

        except Exception as e:
            logger.exception(
                "Error when processing question-answer generation with litellm",
                extra={
                    "week_number": inputs.week_number,
                    "course_code": inputs.course_code,
                    "topic_name": inputs.topic.name,
                    "error": str(e),
                } 
            )
            raise e

# from lite_llm import LiteLLMSetting
# from pydantic import HttpUrl, SecretStr
# from chromadb import HttpClient
# import os 

# async def main():
#     litellm_setting = LiteLLMSetting(
#         url=HttpUrl("http://localhost:9510"),
#         token=SecretStr("abc123"),
#         model="gpt-4o-mini",
#         frequency_penalty=0.0,
#         n=1,
#         temperature=0.0,
#         top_p=1.0,
#         max_completion_tokens=10000,
#         dimension=1024,
#         embedding_model="qwen3-embedding:0.6b"
#     )

#     litellm_service = LiteLLMService(litellm_setting=litellm_setting)
    
#     qa_service = QuestionAnswerGeneratorService(
#         litellm_service=litellm_service,
#         settings=QuestionAnswerGeneratorSetting(
#             model="gpt-4o-mini",
#             temperature=0.5,
#             top_p=1.0,
#             n=1,
#             frequency_penalty=0.0,
#             max_completion_tokens=2000,
#             # reasoning_effort="medium"
#         )
#     )
#     course_code = "rl2025"
#     for week_number in range(1, 9):
#         with open(f'/home/lehoangvu/KLTN/outputs/gpt-4o-mini/{course_code}/week{week_number}_pipeline.json', 'r') as f:
#             data = json.load(f)
            
#         topics = [Topic(**question['topic']) for question in data['questions']]
        
#         analysis_results = []
#         for topic in topics:
#             output_with_context = await qa_service.process(
#                 inputs=QuestionAnswerGeneratorInput(
#                     topic=topic,
#                     week_number=week_number,
#                     course_code=course_code
#                 ),
#                 get_rag_context=True
#             )
        
#             output_without_context = await qa_service.process(
#                 inputs=QuestionAnswerGeneratorInput(
#                     topic=topic,
#                     week_number=week_number,
#                     course_code=course_code
#                 ),
#                 get_rag_context=False
#             )
#             analysis_results.append({
#                 "topic_description": topic.description,
#                 "output_with_context": {
#                     "question": output_with_context.question_answer.question,
#                     "answer": output_with_context.question_answer.answer,
#                     "rag_context": output_with_context.rag_context
#                 },
#                 "output_without_context": {
#                     "question": output_without_context.question_answer.question,
#                     "answer": output_without_context.question_answer.answer
#                 }
#             })

#         if not os.path.exists(f'/home/lehoangvu/KLTN/outputs/context_analysis/{course_code}'):
#             os.makedirs(f'/home/lehoangvu/KLTN/outputs/context_analysis/{course_code}')

#         with open(f'/home/lehoangvu/KLTN/outputs/context_analysis/{course_code}/week{week_number}_analysis.json', 'w', encoding='utf-8') as f:
#             json.dump(analysis_results, f, ensure_ascii=False, indent=4)

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())