#!/bin/python3
from fastapi import FastAPI
from langserve import add_routes

from chains.weather_assistant import OllamaWeatherAssistantChain

app = FastAPI(title='llm playground', version='0.0.1')


def register():
    ollama_weather_chain = OllamaWeatherAssistantChain()
    add_routes(app, ollama_weather_chain, path="/weather")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=9010)
