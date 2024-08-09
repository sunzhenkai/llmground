#!/bin/python3
from typing import List

from langchain_core.tools import BaseTool
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents import AgentExecutor

from agents.tools.weather_tools import get_weather_info
from chains.weather_assistant import OllamaWeatherAssistantChain
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser


class WeatherAssistantAgent:
    def __init__(self):
        self.tools = [get_weather_info]
        self.chain = OllamaWeatherAssistantChain()
        self.chain.llm.llm.bind(functions=[convert_to_openai_function(i) for i in self.tools])
        self.agent = ({
                          "location": lambda x: x["location"],
                          "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                              x["intermediate_steps"]
                          ),
                      } | self.chain.chain.prompt | self.chain.llm.llm | OpenAIToolsAgentOutputParser)
        self.agent = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)
