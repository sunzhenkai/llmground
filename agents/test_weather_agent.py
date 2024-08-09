import json
from unittest import TestCase

from agents.weather_agent import WeatherAssistantAgent


class TestWeatherAssistantAgent(TestCase):
    def test_weather_assistant_agent(self):
        agent = WeatherAssistantAgent()
        # message = agent.executor.invoke({"input": "我现在位于北京"})
        # print(json.dumps(message, indent=4, ensure_ascii=False))

        message = agent.executor.invoke({"input": "我将要前往上海出差"})
        print(json.dumps(message, indent=4, ensure_ascii=False))

    def test_weather_assistant_agent_self(self):
        agent = WeatherAssistantAgent()
        print(agent.invoke({"input": "我将要前往上海出差"}))
