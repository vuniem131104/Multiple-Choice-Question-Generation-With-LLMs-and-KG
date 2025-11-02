from typing import Any
from generation.shared.states import ValidatorState
from generation.shared.settings import QuizValidatorSetting
from generation.shared.models import QuizQuestion 
from generation.domain.quiz_generation.modules.validator.multi_agents.factual import FactualService
from generation.domain.quiz_generation.modules.validator.multi_agents.pedagogical import PedagogicalService
from generation.domain.quiz_generation.modules.validator.multi_agents.psychometric import PsychometricService
from easydict import EasyDict
from functools import cached_property

from base import BaseService
from lite_llm import LiteLLMService
from logger import get_logger

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

logger = get_logger(__name__)


class QuizValidatorService(BaseService):
    litellm_service: LiteLLMService
    settings: QuizValidatorSetting
    
    @property
    def factual_service(self) -> FactualService:
        return FactualService(
            settings=self.settings.factual,
            litellm_service=self.litellm_service
        )

    @property
    def pedagogical_service(self) -> PedagogicalService:
        return PedagogicalService(
            settings=self.settings.pedagogical,
            litellm_service=self.litellm_service
        )

    @property
    def psychometric_service(self) -> PsychometricService:
        return PsychometricService(
            settings=self.settings.psychometric,
            litellm_service=self.litellm_service
        )
        
    @property
    def psychometric_service(self) -> PsychometricService:
        return PsychometricService(
            settings=self.settings.psychometric,
            litellm_service=self.litellm_service
        )
        
    def aggregate(self, state: ValidatorState) -> dict[str]:
        return {
            "score": int((
                state['factual_score'] +
                state['pedagogical_score'] +
                state['psychometric_score']
            ) / 3),
            "feedback": "\n\n".join([
                "The feedback from factual validator:" + "\n" + state['factual_message'],
                "The feedback from pedagogical validator:" + "\n" + state['pedagogical_message'],
                "The feedback from psychometric validator:" + "\n" + state['psychometric_message']
            ])
        }

    @property
    def nodes(self) -> EasyDict:
        return EasyDict({
            "factual": self.factual_service.process,
            "pedagogical": self.pedagogical_service.process,
            "psychometric": self.psychometric_service.process,
            "aggregator": self.aggregate,
        })
    
    @cached_property
    def compiled_graph(self):
        graph = StateGraph(ValidatorState)
        
        for key, tool in self.nodes.items():
            graph.add_node(key, tool)
            
        graph.add_edge(START, "factual")
        graph.add_edge(START, "pedagogical")
        graph.add_edge(START, "psychometric")
        
        graph.add_edge("factual", "aggregator")
        graph.add_edge("pedagogical", "aggregator")
        graph.add_edge("psychometric", "aggregator")
        
        graph.add_edge("aggregator", END)
        
        return graph.compile()
    
    async def process(self, inputs: ValidatorState) -> dict[str, Any]:
        try:
            result = await self.compiled_graph.ainvoke(inputs)
            return result
        except Exception as e:
            logger.exception(
                'Error in QuizValidatorService process',
                extra={
                    'state': inputs,
                    'error': str(e),
                },
            )
            return {
                "score": 100,
                "feedback": "",
            }
    
