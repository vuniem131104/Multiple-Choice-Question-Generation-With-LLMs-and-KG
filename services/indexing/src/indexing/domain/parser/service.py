from __future__ import annotations
import json 
from indexing.domain.parser.prompts import PDF_EXTRACTION_PROMPT
import base64
from storage.minio import MinioService
from storage.minio import MinioInput
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import Role 
from lite_llm import CompletionMessage
from base import BaseModel
from base import BaseService
import os 
import shutil
from logger import get_logger

from indexing.shared.settings.parser import ParserSetting

logger = get_logger(__name__)

class ParserInput(BaseModel):
    course_code: str
    
class ParserOutput(BaseModel):
    contents: str
    course_code: str
    

class ParserService(BaseService):
    litellm_service: LiteLLMService
    minio_service: MinioService
    settings: ParserSetting
    

    async def process(self, inputs: ParserInput) -> ParserOutput:
        if not os.path.exists(self.settings.upload_folder_path):
            os.makedirs(self.settings.upload_folder_path)

        file_path = f"{self.settings.upload_folder_path}/book.pdf"

        try:
            _ = self.minio_service.download_file(
                MinioInput(
                    bucket_name=inputs.course_code, 
                    object_name="book.pdf",
                    file_path=file_path
                )
            )
            
            with open(file_path, "rb") as f:
                pdf_bytes = f.read()
                
            # demo_prompt = "Extract the content in this file. The output is in markdown format."
                
            output = await self.litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.USER,
                            content=PDF_EXTRACTION_PROMPT
                        ),
                        CompletionMessage(
                            role=Role.USER,
                            file_url=f"data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode('utf-8')}"
                        )
                    ],
                    model="gemini-2.5-flash",
                    temperature=0.0,
                    top_p=1.0,
                    n=1,
                    frequency_penalty=0.0,
                    max_completion_tokens=20000,
                )
            )

            return ParserOutput(
                contents=output.response,
                course_code=inputs.course_code,
            )
            
        except Exception as e:
            logger.exception(
                "Error while processing file",
                extra={
                    "course_code": inputs.course_code,
                    "error": str(e)
                }
            )
            return ParserOutput(
                contents="",
                course_code=inputs.course_code,
            )
        finally:
            if os.path.exists(self.settings.upload_folder_path):
                shutil.rmtree(self.settings.upload_folder_path)

# if __name__ == "__main__":
#     from lite_llm import LiteLLMSetting
#     from pydantic import HttpUrl, SecretStr
#     from storage.minio import MinioInput, MinioService, MinioSetting
#     import asyncio

#     minio_setting = MinioSetting(
#         endpoint="localhost:9000",
#         access_key="minioadmin",
#         secret_key="minioadmin123",
#         secure=False,
#     )
            
#     minio_service = MinioService(settings=minio_setting)

#     litellm_setting = LiteLLMSetting(
#         url=HttpUrl("http://localhost:9510"),
#         token=SecretStr("abc123"),
#         model="gemini-2.5-flash",
#         frequency_penalty=0.0,
#         n=1,
#         temperature=0.0,
#         top_p=1.0,
#         max_completion_tokens=10000,
#         dimension=1024,
#         embedding_model="qwen3-embedding:0.6b"
#     )

#     litellm_service = LiteLLMService(litellm_setting=litellm_setting)
    
#     settings = ParserSetting(
#         upload_folder_path="upload_files"
#     )
    
#     parser_service = ParserService(
#         litellm_service=litellm_service,
#         minio_service=minio_service,
#         settings=settings
#     )
    
#     output = asyncio.run(
#         parser_service.process(
#             inputs=ParserInput(
#                 course_code="int3405"
#             )
#         )
#     )
    
#     print(output)