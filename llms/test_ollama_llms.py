from unittest import TestCase

from llms.ollama_llms import OllamaWrapper


class TestOllamaWrapper(TestCase):
    def test_init(self):
        ollama_llm = OllamaWrapper()
        print(ollama_llm.llm.invoke('你好'))
