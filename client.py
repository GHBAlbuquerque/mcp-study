import asyncio
from pathlib import Path

from fastmcp import Client

server_path = Path(__file__).parent / "server.py"
client = Client(server_path)

async def call_server(client: Client, username: str, user_id: int):
    async with client:
        arguments = {"username": username, "user_id": user_id}
        result = await client.call_tool("hello", arguments)
        print(result)

if __name__== "__main__":
      asyncio.run(call_server(client, "gigibene", 123456789))
      
      
