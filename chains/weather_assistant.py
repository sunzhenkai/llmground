#!/bin/python3
from typing import Dict, Any, Optional, List

from langchain.chains.base import Chain
from langchain_core.callbacks import CallbackManagerForChainRun, AsyncCallbackManagerForChainRun
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from llms.ollama_llms import OllamaWrapper
from pydantic.v1 import BaseModel


class WeatherAssistantChain(Chain):
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", """你是一个贴心的中文天气助手， 简明扼要地提醒用户需要关注的天气信息"""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
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

    def _acall(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        raise NotImplementedError()


class OllamaWeatherAssistantChain:
    def __init__(self, *args, **kwargs):
        self.llm = OllamaWrapper(*args, **kwargs)
        self.chain = WeatherAssistantChain(llm=self.llm.llm)
