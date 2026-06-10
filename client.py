import asyncio

from fastmcp import Client
from openai import OpenAI

import dotenv
import os

dotenv.load_dotenv()

server_path = "http://localhost:8000/sse"
client = Client(server_path)

async def call_server(client: Client, search: str,):
    api_key=os.getenv("OPENAI_API_KEY")
    
    
    async with client:
        arguments = {"search": search}
        result = await client.call_tool("search_wikipedia", arguments)
        print(f'\n==================================================================\n')
        print(result)
        system_message=f"""
            You are a bot that runs searches on wikipedia.
            User has searched: {search}
            For this search, you received the following answer: {result}
            Format a friendly response to the user based on the search result.
        """
        
        client_openai=OpenAI(api_key=api_key)
        
        response=client_openai.responses.create(
            model="gpt-5-nano",
            instructions=system_message,
            input="Please summarize this search result for me.",
        )
        print(f'\n==================================================================\n')
        print(response.output_text)
        
        

if __name__== "__main__":
      asyncio.run(call_server(client, "Broken Earth Series"))
      
      
