import json 

folder = '/home/lehoangvu/KLTN/outputs/context_analysis/rl2025'
with_context_question_relevances = []
without_context_question_relevances = []
useful_counts = 0
for week_number in range(1, 9):
    
    with open(f'{folder}/week{week_number}_kg_evaluation.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    useful_count = sum(1 for item in data if item['evaluation']['is_useful'] == 'Yes')
    useful_counts += useful_count
    # pipeline_win = sum(1 for item in data if item['evaluation']['winner'] == 'pipeline')
    # baseline_win = sum(1 for item in data if item['evaluation']['winner'] == 'baseline')
    # ties = sum(1 for item in data if item['evaluation']['winner'] == 'tie')

    with_context_question_relevances.extend([item['evaluation']['with_context_question_relevance'] for item in data])
    without_context_question_relevances.extend([item['evaluation']['without_context_question_relevance'] for item in data])

print("Percentage of Useful KG:", useful_counts / len(with_context_question_relevances))
print("Mean With Context Question Relevance:", sum(with_context_question_relevances) / len(with_context_question_relevances))
print("Mean Without Context Question Relevance:", sum(without_context_question_relevances) / len(without_context_question_relevances))