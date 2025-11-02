from generation.domain.llm_as_judge.prompts import LLM_AS_JUDGE_PAIRWISE_USER_PROMPT
from generation.domain.llm_as_judge.prompts import LLM_AS_JUDGE_QUESTION_PAIR_TEMPLATE
from generation.domain.llm_as_judge.prompts import LLM_AS_JUDGE_PAIRWISE_COMPARISON_PROMPT
from typing import Any
from base import BaseModel
from base import BaseService
from lite_llm import LiteLLMService
from lite_llm import LiteLLMInput
from lite_llm import CompletionMessage
from generation.shared.settings import JudgeSetting
from lite_llm import Role
from logger import get_logger


logger = get_logger(__name__)

class QuizEvaluationInput(BaseModel):
    topics: list[dict[str, Any]]
    pipeline_questions: list[dict[str, Any]]
    baseline_questions: list[dict[str, Any]]
    
class QuizCriteria(BaseModel):
    relevance: float
    clarity: float
    distractor_plausibility: float
    difficulty: float
    bloom_level_appropriateness: float
    
class Comparison(BaseModel):
    question_number: int
    topic_name: str
    pipeline_scores: QuizCriteria
    baseline_scores: QuizCriteria
    winner: str
    rationale: str
    
class QuizEvaluationOutput(BaseModel):
    comparisons: list[Comparison]
    
    
class QuizEvaluatorService(BaseService):
    litellm_service: LiteLLMService
    settings: JudgeSetting
    
    async def process(self, inputs: QuizEvaluationInput) -> QuizEvaluationOutput:
        topics_list = "\n".join(
            [f"- {topic['name']}: {topic['description']}" for topic in inputs.topics]
        )
        
        question_pairs = ""
        num_pairs = min(len(inputs.pipeline_questions), len(inputs.baseline_questions))
        for i in range(num_pairs):
            pipeline_q = inputs.pipeline_questions[i]
            baseline_q = inputs.baseline_questions[i]
            topic = inputs.topics[i]
            question_pairs += LLM_AS_JUDGE_QUESTION_PAIR_TEMPLATE.format(
                pair_number=i+1,
                topic_name=topic.get('name', 'N/A'),
                topic_description=topic.get('description', 'N/A'),
                difficulty=topic.get('difficulty_level', 'N/A'),
                bloom_level=topic.get('bloom_taxonomy_level', 'N/A'),
                pipeline_question=pipeline_q['question'],
                pipeline_answer=pipeline_q['answer'],
                pipeline_distractors="\n".join([f"- {d}" for d in pipeline_q['distractors']]),
                baseline_question=baseline_q['question'],
                baseline_answer=baseline_q['answer'],
                baseline_distractors="\n".join([f"- {d}" for d in baseline_q['distractors']]),
            )
        
        user_prompt = LLM_AS_JUDGE_PAIRWISE_USER_PROMPT.format(
            num_pairs=num_pairs,
            topics_list=topics_list,
            question_pairs=question_pairs
        )
        
        
        response = await self.litellm_service.process_async(
            inputs=LiteLLMInput(
                model=self.settings.model,
                messages=[
                    CompletionMessage(role=Role.SYSTEM, content=LLM_AS_JUDGE_PAIRWISE_COMPARISON_PROMPT),
                    CompletionMessage(role=Role.USER, content=user_prompt)
                ],
                response_format=QuizEvaluationOutput,
                temperature=self.settings.temperature,
                max_completion_tokens=self.settings.max_completion_tokens,
                top_p=self.settings.top_p,
                frequency_penalty=self.settings.frequency_penalty,
                n=self.settings.n,
                reasoning_effort=self.settings.reasoning_effort,
            )
        )
        
        return response.response
    
if __name__ == "__main__":
    from lite_llm import LiteLLMSetting
    import asyncio
    import json 
    from pydantic import HttpUrl, SecretStr


    litellm_setting = LiteLLMSetting(
        url=HttpUrl("http://localhost:9510"),
        token=SecretStr("abc123"),
        model="gemini-2.5-flash",
        frequency_penalty=0.0,
        n=1,
        temperature=0.0,
        top_p=1.0,
        max_completion_tokens=10000,
        dimension=1536,
        embedding_model="gemini-embedding"
    )
    
    litellm_service = LiteLLMService(litellm_setting=litellm_setting)
    
    llm_as_judge_service = QuizEvaluatorService(
        litellm_service=litellm_service
    )
    
    week_number = 3
    course_code = "int3405"

    with open(f"/home/lehoangvu/KLTN/MCQs_4o_mini/{course_code}/week{week_number}_pipeline.json", "r", encoding='utf-8') as f:
        pipeline_output = json.load(f)
        
    topics = [item['topic'] for item in pipeline_output['questions']]
    pipeline_questions = [
        {
            "question": item['question'],
            "answer": item['answer'],
            "distractors": item['distractors']
        }
        for item in pipeline_output['questions']
    ]

    with open(f"/home/lehoangvu/KLTN/MCQs_4o_mini/{course_code}/week{week_number}_baseline.json", "r", encoding='utf-8') as f:
        baseline_questions = json.load(f)
        
    baseline_questions = baseline_questions['questions']
    
    async def test():
        output = await llm_as_judge_service.process(
            inputs=QuizEvaluationInput(
                topics=topics,
                pipeline_questions=pipeline_questions,
                baseline_questions=baseline_questions
            )
        )
        with open(f"MCQs_4o_mini/{course_code}/week{week_number}_evaluation.json", "w", encoding='utf-8') as f:
            json.dump(output.model_dump(), f, ensure_ascii=False, indent=4)
    asyncio.run(test())
    