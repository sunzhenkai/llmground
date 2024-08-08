from unittest import TestCase

from chains.weather_assistant import OllamaWeatherAssistantChain


class TestOllamaWeatherAssistantChain(TestCase):
    def test_init(self):
        chain = OllamaWeatherAssistantChain()
        print(chain)
