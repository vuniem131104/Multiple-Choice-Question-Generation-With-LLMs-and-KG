from __future__ import annotations

from chromadb.api import ClientAPI
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
    

class QuestionAnswerGeneratorService(BaseService):
    litellm_service: LiteLLMService
    settings: QuestionAnswerGeneratorSetting
    chromadb_client: ClientAPI

    async def _get_rag_context(self, query: str) -> Optional[str]:
        """
        Gọi RAG API để lấy context liên quan đến query
        """
        # try:
        #     rag_url = "http://0.0.0.0:3005/v1/local_search"
            
        #     async with httpx.AsyncClient(timeout=30.0) as client:
        #         response = await client.post(
        #             rag_url,
        #             headers={
        #                 "accept": "application/json",
        #                 "Content-Type": "application/json"
        #             },
        #             json={"query": query}
        #         )
                
        #         if response.status_code == 200:
        #             result = response.json()
                    
        #             # Build context string từ kết quả RAG
        #             context_parts = []
                    
        #             if "chunk_df" in result and result["chunk_df"]:
        #                 for chunk_data in result["chunk_df"]:
        #                     if "chunk" in chunk_data:
        #                         context_parts.append(f"**Nội dung từ tài liệu:**\n{chunk_data['chunk']}")
                            
        #                     if "entities" in chunk_data and chunk_data["entities"]:
        #                         entities_text = "\n".join([f"- {entity}" for entity in chunk_data["entities"]])
        #                         context_parts.append(f"**Các khái niệm quan trọng:**\n{entities_text}")
                            
        #                     if "relationships" in chunk_data and chunk_data["relationships"]:
        #                         relationships_text = "\n".join([f"- {rel}" for rel in chunk_data["relationships"]])
        #                         context_parts.append(f"**Mối quan hệ:**\n{relationships_text}")
                    
        #             if context_parts:
        #                 return "\n\n".join(context_parts)
        #             else:
        #                 logger.warning(
        #                     "RAG API returned empty or invalid context",
        #                     extra={"query": query, "response": result}
        #                 )
        #                 return None
                        
        #         else:
        #             logger.warning(
        #                 "RAG API call failed",
        #                 extra={"query": query, "status_code": response.status_code, "response": response.text}
        #             )
        #             return None
                    
        # except Exception as e:
        #     logger.exception(
        #         "Error calling RAG API",
        #         extra={"query": query, "error": str(e)}
        #     )
        #     return None
        return None

    async def process(self, inputs: QuestionAnswerGeneratorInput) -> QuestionAnswerGeneratorOutput:
        # Lấy RAG context
        rag_context = await self._get_rag_context(inputs.topic.name)
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    "http://quiz_generation:3005/query",
                    headers={
                        "accept": "application/json",
                        "Content-Type": "application/json"
                    },
                    json={
                        "course_code": inputs.course_code,
                        "query": inputs.topic.name,
                    }
                )
                
                if response.status_code == 200:
                    results = response.json()['results']
                else:
                    logger.warning(
                        "Failed to retrieve similar questions from quiz_generation service",
                        extra={
                            "course_code": inputs.course_code,
                            "week_number": inputs.week_number,
                            "topic_name": inputs.topic.name,
                            "status_code": response.status_code,
                            "response": response.text
                        }
                    )
                    results = {"documents": [[]], "metadatas": [[]]}
            
            examples: list[tuple[str, str]] = []
            
            for document, metadata in zip(results['documents'][0], results['metadatas'][0]):
                examples.append((document, metadata['answer']))
                
            if examples:
                formatted_examples = "Dưới đây là một số ví dụ về các cặp câu hỏi-câu trả lời chất lượng cao để hướng dẫn việc tạo ra của bạn:\n\n" + "\n\n".join(
                    [f"Ví dụ {i+1}:\nCâu hỏi: {q}\nCâu trả lời: {a}" for i, (q, a) in enumerate(examples)]
                ) + "\n\nSử dụng những ví dụ này làm tham khảo cho phong cách, độ rõ ràng và tính phù hợp của câu hỏi và câu trả lời. Tạo ra một cặp câu hỏi-câu trả lời chất lượng tương tự cho chủ đề đã cho."
            else:
                formatted_examples = "Không có ví dụ tương tự nào. Tạo ra một cặp câu hỏi-câu trả lời chất lượng cao dựa trên hướng dẫn ở trên."

            logger.info(
                "Retrieved similar questions from database",
                extra={
                    "course_code": inputs.course_code,
                    "week_number": inputs.week_number,
                    "topic_name": inputs.topic.name,
                    "similar_questions_count": len(examples),
                    "formatted_examples": formatted_examples,
                    "rag_context_available": rag_context is not None
                }
            )
        except Exception as e:
            logger.exception(
                "Error when retrieving similar questions from database",
                extra={
                    "week_number": inputs.week_number,
                    "course_code": inputs.course_code,
                    "topic_name": inputs.topic.name,
                    "error": str(e),
                } 
            )
            formatted_examples = "Không có ví dụ tương tự nào. Tạo ra một cặp câu hỏi-câu trả lời chất lượng cao dựa trên hướng dẫn ở trên."
            
        try:
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    model=self.settings.model,
                    messages=[
                        CompletionMessage(
                            role=Role.SYSTEM,
                            content=QUESTION_ANSWER_SYSTEM_PROMPT.format(
                                examples=formatted_examples
                            )
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
                course_code=inputs.course_code
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


