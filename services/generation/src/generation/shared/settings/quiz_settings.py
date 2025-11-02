from __future__ import annotations 

from base import BaseModel
from .concept_card import ConceptCardExtractorSetting
from .topic_generator import TopicGeneratorSetting
from .question_answer_generator import QuestionAnswerGeneratorSetting
from .explanation import ExplanationGeneratorSetting
from .distractors import DistractorsGeneratorSetting
from .quiz_validator import QuizValidatorSetting
from .quiz_correction import QuizCorrectionSetting

class QuizGenerationSetting(BaseModel):
    concept_card_extractor: ConceptCardExtractorSetting
    topic_generator: TopicGeneratorSetting
    question_answer_generator: QuestionAnswerGeneratorSetting
    explanation_generator: ExplanationGeneratorSetting
    distractors_generator: DistractorsGeneratorSetting
    validator: QuizValidatorSetting
    correction: QuizCorrectionSetting
    max_feedback_attempts: int
    acceptance_score_threshold: int
    max_concurrent_tasks: int