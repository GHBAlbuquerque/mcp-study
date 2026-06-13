import os

import dotenv
import requests
from fastmcp import FastMCP

mcp_server = FastMCP("mcp-server")

@mcp_server.tool()
async def search_local_weather(local: str) -> dict:
    dotenv.load_dotenv()
    api_key=os.getenv("OPEN_WEATHER_API_KEY")
    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q": local,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(url=url, params=params)
    return response.json()

@mcp_server.tool()
async def search_weather_forecast(local: str) -> dict:
    dotenv.load_dotenv()
    api_key=os.getenv("OPEN_WEATHER_API_KEY")
    url="https://api.openweathermap.org/data/2.5/forecast"
    params={
        "q": local,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(url=url, params=params)
    return response.json()

if __name__ == "__main__":
    mcp_server.run(transport="sse")