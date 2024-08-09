#!/bin/python3
"""
REF 1: https://github.com/langchain-ai/langserve/blob/main/examples/configurable_agent_executor/server.py
"""
from typing import Any, Optional, List, AsyncIterator, cast, Dict

from langchain.agents import AgentExecutor
from langchain_core.runnables import Runnable, RunnableConfig, ensure_config
from langchain_core.runnables.utils import Input, Output, ConfigurableFieldSpec

from agents.agent_tools import create_tools_agent
from agents.tools.weather_tools import get_weather_info
from chains.weather_assistant import OllamaWeatherAssistantChain


class WeatherAssistantAgent(Runnable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tools = [get_weather_info]
        self.chain = OllamaWeatherAssistantChain()
        # self.chain.llm.llm.bind_tools(self.tools)
        # self.agent = (self.chain.chain.prompt | self.chain.llm.llm | AgentOutputParser())
        self.agent = create_tools_agent(self.chain.llm.llm, self.tools, prompt=self.chain.chain.prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=self.tools)

    def _create_executor(self, config: Optional[RunnableConfig] = None) -> AgentExecutor:
        config = ensure_config(config)
        configurable = cast(Dict[str, Any], config.pop("configurable", {}))

        if configurable:
            configured_agent = self.agent.with_config(
                {
                    "configurable": configurable,
                }
            )
        else:
            configured_agent = self.agent

        return AgentExecutor(
            agent=configured_agent,
            tools=self.tools,
        )

    def invoke(self, input: Input, config: Optional[RunnableConfig] = None) -> Output:
        response = self._create_executor(config).invoke(input, config)
        return response['output']

    @property
    def config_specs(self) -> List[ConfigurableFieldSpec]:
        return self.agent.config_specs

    async def astream(
            self,
            input: Input,
            config: Optional[RunnableConfig] = None,
            **kwargs: Optional[Any],
    ) -> AsyncIterator[Output]:
        async for output in self._create_executor(config).astream(input, config=config, **kwargs):
            if 'output' in output:
                yield output['output']
