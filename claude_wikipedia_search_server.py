from fastmcp import FastMCP
from wikipedia import wikipedia


server_mcp = FastMCP("mcp-server")

@server_mcp.tool() # mcp servers run async to avoid blocking, so all tools should be async
async def search_wikipedia(search: str) -> str: #adding types helps IA undestand what the function does
	"""Return a short Wikipedia summary for a search term.

	Args:
		search (str): Topic or phrase to look up on Wikipedia.

	Returns:
		str: Plain-text summary extracted from Wikipedia.
	"""
	return wikipedia.summary(search)


if __name__ == "__main__":
	server_mcp.run(transport="stdio") #standard input output
 
 