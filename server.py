from fastmcp import FastMCP

server_mcp = FastMCP("mcp-local")

@server_mcp.tool() # mcp servers run async to avoid blocking, so all tools should be async
async def hello(username: str, user_id: int) -> str: #typing helps IA undestand what the function does
	return f'Hello {username}! (ID {user_id})'

if __name__ == "__main__":
	server_mcp.run(transport="stdio") #standard input output
 
 