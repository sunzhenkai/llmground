#!/bin/python3
from langchain.agents import AgentExecutor, create_tool_calling_agent
from agents.tools.weather_tools import get_weather_info
from chains.weather_assistant import OllamaWeatherAssistantChain


class WeatherAssistantAgent:
    def __init__(self):
        self.tools = [get_weather_info]
        self.chain = OllamaWeatherAssistantChain()
        self.agent = create_tool_calling_agent(self.chain.llm.llm, self.tools, prompt=self.chain.chain.prompt)
        self.agent = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)
