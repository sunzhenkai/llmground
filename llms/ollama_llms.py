#!/bin/python3
from langchain_ollama.chat_models import ChatOllama
import os

OLLAMA_DEFAULT_MODEL = os.getenv('OLLAMA_DEFAULT_MODEL', "llama3.1:8b")
# OLLAMA_DEFAULT_MODEL="qwen2:7b"
OLLAMA_SERVER_URL = os.getenv('OLLAMA_SERVER_URL', "http://127.0.0.1:11434")


class OllamaWrapper:
    def __init__(self, url=OLLAMA_SERVER_URL, model=OLLAMA_DEFAULT_MODEL):
        self.llm = ChatOllama(model=model, base_url=url)
