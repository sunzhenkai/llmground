#!/bin/python3
from langchain_community.llms import Ollama
import os

OLLAMA_SERVER_URL = os.getenv('OLLAMA_SERVER_URL', "http://127.0.0.1:11434")


class OllamaWrapper:
    def __init__(self, url=OLLAMA_SERVER_URL, model="qwen2:7b"):
        self.llm = Ollama(model=model, base_url=url)
