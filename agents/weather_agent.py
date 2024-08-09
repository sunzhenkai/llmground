#!/bin/python3
from typing import Any

from langchain.agents import AgentExecutor, create_tool_calling_agent
from pydantic.v1 import BaseModel

from agents.agent_tools import create_tools_agent
from agents.tools.weather_tools import get_weather_info
from chains.weather_assistant import OllamaWeatherAssistantChain


class WeatherAssistantAgent:
    class Output(BaseModel):
        output: Any

    def __init__(self):
        self.tools = [get_weather_info]
        self.chain = OllamaWeatherAssistantChain()
        # self.chain.llm.llm.bind_tools(self.tools)
        # self.agent = (self.chain.chain.prompt | self.chain.llm.llm | AgentOutputParser())
        self.agent = create_tools_agent(self.chain.llm.llm, self.tools, prompt=self.chain.chain.prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=self.tools)
