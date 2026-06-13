import asyncio

from fastmcp import Client
from openai import OpenAI

import dotenv
import os

dotenv.load_dotenv()

server_path = "http://localhost:8000/sse"
client = Client(server_path)

async def call_server(client: Client, local: str,):
    api_key=os.getenv("OPENAI_API_KEY")
    
    async with client:
        arguments = {"local": local}
        local_weather = await client.call_tool("search_local_weather", arguments)
        weather_forecast = await client.call_tool("search_weather_forecast", arguments)

        #print(local_weather)
        #print(f'\n==================================================================\n')
        #print(weather_forecast)
        
        print(f'\n==================================================================\n')
        system_message=f"""
            You are a bot that runs weather forecast searches.
            User has searched: {local}
            For this search, you received the following answers for local weather and weather forecast: {local_weather} and {weather_forecast}
            Format a friendly response to the user based on the search result.
        """
        
        client_openai=OpenAI(api_key=api_key)
        
        response=client_openai.responses.create(
            model="gpt-5-nano",
            instructions=system_message,
            input="What is the current and forecast weather for the location provided?",
        )
        print(f'\n==================================================================\n')
        print(response.output_text)
        
        

if __name__== "__main__":
      asyncio.run(call_server(client, "Osasco, São Paulo, Brazil"))
      
      
