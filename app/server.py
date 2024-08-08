from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from chains.weather_assistant import OllamaWeatherAssistantChain

app = FastAPI(title='llm playground', version='0.0.1')


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# weather assistant
ollama_weather_chain = OllamaWeatherAssistantChain()
add_routes(app, ollama_weather_chain.chain, path="/weather")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9010)
