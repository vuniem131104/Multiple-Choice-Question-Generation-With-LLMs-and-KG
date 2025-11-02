import json 
from base import BaseModel 
from base import BaseService 
from typing import Any

class AnalysisInput(BaseModel):
    start_week: int 
    end_week: int 
    course_code: str 
    mcqs_folder: str
    
class AnalysisOutput(BaseModel):
    results: list[dict[str, Any]] 

class AnalysisService(BaseService):
    
    def process(self, inputs: AnalysisInput) -> AnalysisOutput:
        results = []
        avg_relevance_baselines = []
        avg_relevance_pipelines = []
        avg_clarity_pipelines = []
        avg_clarity_baselines = []
        avg_distractor_plausibility_pipelines = []
        avg_distractor_plausibility_baselines = []
        avg_difficulty_pipelines = []
        avg_difficulty_baselines = []
        avg_bloom_level_appropriateness_pipelines = []
        avg_bloom_level_appropriateness_baselines = []

        for week_number in range(inputs.start_week, inputs.end_week + 1):
            with open(f'{inputs.mcqs_folder}/{inputs.course_code}/week{week_number}_evaluation.json') as f:
                evaluation_output = json.load(f)
                
            total_pipeline_wins = sum(1 for item in evaluation_output['comparisons'] if item['winner'] == 'pipeline')
            total_baseline_wins = sum(1 for item in evaluation_output['comparisons'] if item['winner'] == 'baseline')
            total_ties = sum(1 for item in evaluation_output['comparisons'] if item['winner'] == 'tie')
            
            total_questions = len(evaluation_output['comparisons'])
                
            percentage_pipeline_wins = (total_pipeline_wins / total_questions) * 100
            percentage_baseline_wins = (total_baseline_wins / total_questions) * 100
            percentage_ties = (total_ties / total_questions) * 100
            
            relevance_scores_pipeline = [item['pipeline_scores']['relevance'] for item in evaluation_output['comparisons']]
            relevance_scores_baseline = [item['baseline_scores']['relevance'] for item in evaluation_output['comparisons']]
            avg_relevance_pipeline = sum(relevance_scores_pipeline) / total_questions
            avg_relevance_baseline = sum(relevance_scores_baseline) / total_questions
            avg_relevance_pipelines.append(avg_relevance_pipeline)
            avg_relevance_baselines.append(avg_relevance_baseline)
            
            clarity_scores_pipeline = [item['pipeline_scores']['clarity'] for item in evaluation_output['comparisons']]
            clarity_scores_baseline = [item['baseline_scores']['clarity'] for item in evaluation_output['comparisons']]
            avg_clarity_pipeline = sum(clarity_scores_pipeline) / total_questions
            avg_clarity_baseline = sum(clarity_scores_baseline) / total_questions
            avg_clarity_pipelines.append(avg_clarity_pipeline)
            avg_clarity_baselines.append(avg_clarity_baseline)

            distractor_plausibility_scores_pipeline = [item['pipeline_scores']['distractor_plausibility'] for item in evaluation_output['comparisons']]
            distractor_plausibility_scores_baseline = [item['baseline_scores']['distractor_plausibility'] for item in evaluation_output['comparisons']]
            avg_distractor_plausibility_pipeline = sum(distractor_plausibility_scores_pipeline) / total_questions
            avg_distractor_plausibility_baseline = sum(distractor_plausibility_scores_baseline) / total_questions
            avg_distractor_plausibility_pipelines.append(avg_distractor_plausibility_pipeline)
            avg_distractor_plausibility_baselines.append(avg_distractor_plausibility_baseline)
            
            difficulty_scores_pipeline = [item['pipeline_scores']['difficulty'] for item in evaluation_output['comparisons']]
            difficulty_scores_baseline = [item['baseline_scores']['difficulty'] for item in evaluation_output['comparisons']]
            avg_difficulty_pipeline = sum(difficulty_scores_pipeline) / total_questions
            avg_difficulty_baseline = sum(difficulty_scores_baseline) / total_questions
            avg_difficulty_pipelines.append(avg_difficulty_pipeline)
            avg_difficulty_baselines.append(avg_difficulty_baseline)
            
            bloom_level_appropriateness_scores_pipeline = [item['pipeline_scores']['bloom_level_appropriateness'] for item in evaluation_output['comparisons']]
            bloom_level_appropriateness_scores_baseline = [item['baseline_scores']['bloom_level_appropriateness'] for item in evaluation_output['comparisons']]
            avg_bloom_level_appropriateness_pipeline = sum(bloom_level_appropriateness_scores_pipeline) / total_questions
            avg_bloom_level_appropriateness_baseline = sum(bloom_level_appropriateness_scores_baseline) / total_questions   
            avg_bloom_level_appropriateness_pipelines.append(avg_bloom_level_appropriateness_pipeline)
            avg_bloom_level_appropriateness_baselines.append(avg_bloom_level_appropriateness_baseline)
            
            overal_analysis = {
                "week_number": week_number,
                "total_questions": total_questions,
                "pipeline_wins": total_pipeline_wins,
                "baseline_wins": total_baseline_wins,
                "ties": total_ties,
                "percentage_pipeline_wins": f"{percentage_pipeline_wins:.2f}%",
                "percentage_baseline_wins": f"{percentage_baseline_wins:.2f}%",
                "percentage_ties": f"{percentage_ties:.2f}%",
                "average_scores": {
                    "relevance": {
                        "pipeline": f"{avg_relevance_pipeline:.4f}",
                        "baseline": f"{avg_relevance_baseline:.4f}"
                    },
                    "clarity": {
                        "pipeline": f"{avg_clarity_pipeline:.4f}",
                        "baseline": f"{avg_clarity_baseline:.4f}"
                    },
                    "distractor_plausibility": {
                        "pipeline": f"{avg_distractor_plausibility_pipeline:.4f}",
                        "baseline": f"{avg_distractor_plausibility_baseline:.4f}"
                    },
                    "difficulty": {
                        "pipeline": f"{avg_difficulty_pipeline:.4f}",
                        "baseline": f"{avg_difficulty_baseline:.4f}"
                    },
                    "bloom_level_appropriateness": {
                        "pipeline": f"{avg_bloom_level_appropriateness_pipeline:.4f}",
                        "baseline": f"{avg_bloom_level_appropriateness_baseline:.4f}"
                    }
                }
            }
            
            results.append(overal_analysis)
            
        return AnalysisOutput(results=results)
    
# if __name__ == "__main__":
#     analysis_service = AnalysisService()
    
#     analysis_output = analysis_service.process(
#         inputs=AnalysisInput(
#             start_week=1, end_week=8, course_code="int3405", mcqs_folder="/home/lehoangvu/KLTN/outputs/gemini-2.5-flash"
#         )
#     )
          
#     print(analysis_output)      