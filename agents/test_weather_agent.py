from unittest import TestCase

from agents.weather_agent import WeatherAssistantAgent


class TestWeatherAssistantAgent(TestCase):
    def test_weather_assistant_agent(self):
        agent = WeatherAssistantAgent()
        agent.agent.invoke({"location": "北京"})
