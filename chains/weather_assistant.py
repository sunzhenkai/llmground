#!/bin/python3
from typing import Dict, Any, Optional, List

from langchain.chains.base import Chain
from langchain_core.callbacks import CallbackManagerForChainRun
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate, PromptTemplate, ChatPromptTemplate

from llms.ollama_llms import OllamaWrapper
from pydantic import field_validator
from langserve.pydantic_v1 import BaseModel


class WeatherAssistantChain(Chain):
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", """你是一个中文天气助手，你需要从工具获取用户指定位置的实时天气。
            并以天气助手的口吻，简介扼要地给出用户需要关注的天气信息。"""),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    output_key: str = 'text'

    class InputSchema(BaseModel):
        input: str

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
        self.chain = WeatherAssistantChain(llm=self.llm.llm)
