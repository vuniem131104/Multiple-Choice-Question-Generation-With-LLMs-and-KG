from lite_llm import LiteLLMEmbeddingInput, LiteLLMService, LiteLLMSetting, CompletionMessage, Role, LiteLLMInput
from pydantic import HttpUrl, SecretStr
from base import BaseModel 
import json

class KnowledgeGraphEvaluationOutput(BaseModel):
    is_useful: str
    usefulness_rationale: str
    with_context_question_relevance: float
    without_context_question_relevance: float

litellm_setting=LiteLLMSetting(
    url=HttpUrl("http://localhost:9510"),
    token=SecretStr("abc123"),
    model="gemini-2.5-flash",
    frequency_penalty=0.0,
    n=1,
    temperature=0.0,
    top_p=1.0,
    max_completion_tokens=10000,
    dimension=1024,
    embedding_model="qwen3-embedding:0.6b",
)

litellm_service = LiteLLMService(litellm_setting=litellm_setting)

LLM_JUDGE_KG = """
You are an expert knowledge graph evaluator. Your task is to assess the quality and accuracy of knowledge graphs based on predefined criteria.
You will be provided two question-answer pairs along with the context from knowledge graph and the topic that they belong to.
The question-answer from the pipeline system that has been generated based on the knowledge graph and the question-answer from the baseline system as below:
The topic is: {topic_name}
The context from knowledge graph is:
{context}
The pipeline question-answer pair is:
Question: {pipeline_question}
Answer: {pipeline_answer}
The baseline question-answer pair is:
Question: {baseline_question}
Answer: {baseline_answer}
Your task is to vote as the following question bellow:
1. Whether the knowledge graph is useful for generating the question-answer pair suitable to the topic?
Answer with "Yes" or "No" and provide a detailed rationale for your decision.
2. Rate the relevance of EACH QUESTION to the TOPIC ONLY for both question-answer pairs on a scale from 0 to 1 (0 being not relevant at all, 1 being highly relevant).
IMPORTANT: When scoring relevance, ONLY compare the question against the topic description. DO NOT consider the context from the knowledge graph in your relevance scoring. The context is only used for evaluating usefulness in task 1.
The output should be in the following JSON format:
```json
{{
  "is_useful": "Yes" or "No",
  "usefulness_rationale": "Detailed explanation of why the knowledge graph is useful or not, referencing specific aspects of the context and question-answer pair.",
  "with_context_question_relevance": float (score from 0 to 1),
  "without_context_question_relevance": float (score from 0 to 1),
}}
```
Note that the question-answer is in the format of multiple choice question. The output must be in Vietnamese.
"""

async def test():
    course_code = "rl2025"
    for week_number in range(1, 9):
        results = []
        with open(f'/home/lehoangvu/KLTN/outputs/context_analysis/{course_code}/week{week_number}_analysis.json', 'r', encoding='utf-8') as f:
            analysis_results = json.load(f)

        for item in analysis_results:

            topic = item['topic_description']
            context = item['output_with_context']['rag_context']

            pipeline_question = item['output_with_context']['question']
            pipeline_answer = item['output_with_context']['answer']
            baseline_question = item['output_without_context']['question']
            baseline_answer = item['output_without_context']['answer']

            response = await litellm_service.process_async(
                inputs=LiteLLMInput(
                    messages=[
                        CompletionMessage(
                            role=Role.USER,
                            content=LLM_JUDGE_KG.format(
                                topic_name=topic,
                                context=context,
                                pipeline_question=pipeline_question,
                                pipeline_answer=pipeline_answer,
                                baseline_question=baseline_question,
                                baseline_answer=baseline_answer,
                            )
                        )
                    ],
                    response_format=KnowledgeGraphEvaluationOutput,
                )
            )
            
            output = response.response
            winner = "pipeline" if output.with_context_question_relevance > output.without_context_question_relevance else "baseline" if output.with_context_question_relevance < output.without_context_question_relevance else "tie"
            
            results.append(
                {
                    "topic_description": topic,
                    "evaluation": {
                        **output.model_dump(),
                        "winner": winner
                    }
                }
            )

        with open(f'/home/lehoangvu/KLTN/outputs/context_analysis/{course_code}/week{week_number}_kg_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test())