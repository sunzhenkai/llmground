#!/bin/python3
from typing import Dict, Any, Optional, List

from langchain.chains.base import Chain
from langchain_core.callbacks import CallbackManagerForChainRun
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate, PromptTemplate
from llms.ollama_llms import OllamaWrapper


class WeatherAssistantChain(Chain):
    llm: BaseLanguageModel = PromptTemplate.from_template("你是一个天气助手")
    prompt: BasePromptTemplate
    output_key: str = 'text'

    @property
    def input_keys(self) -> List[str]:
        return self.prompt.input_variables

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _call(self, inputs: Dict[str, Any], run_manager: Optional[CallbackManagerForChainRun] = None) -> Dict[str, Any]:
        prompt_value = self.prompt.format_prompt(**inputs)
        response = self.llm.generate_prompt([prompt_value], callbacks=run_manager.get_child() if run_manager else None)
        return {self.output_key: response.generations[0][0].text}


class OllamaWeatherAssistantChain:
    def __init__(self, *args, **kwargs):
        self.llm = OllamaWrapper(*args, **kwargs)
        self.chain = WeatherAssistantChain(llm=self.llm)

