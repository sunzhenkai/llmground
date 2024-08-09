from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

from agents.weather_agent import WeatherAssistantAgent
from chains.weather_assistant import WeatherAssistantChain

app = FastAPI(title='llm playground', version='0.0.1')


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# weather assistant
weather_agent = WeatherAssistantAgent()
add_routes(app, weather_agent.executor, path="/weather", input_type=WeatherAssistantChain.InputSchema,
           output_type=WeatherAssistantAgent.Output)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9010)
