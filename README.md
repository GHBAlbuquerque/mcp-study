# MCP Study - Weather & Wikipedia servers

Small study project that exposes lightweight MCP-style tools to fetch current weather, weather forecasts (OpenWeatherMap) and short Wikipedia summaries.

**Contents**
- `claude_weather_forecast_server.py` - MCP server exposing current weather and forecast tools (uses OpenWeatherMap).
- `weather_forecast_server.py` - alternative weather server implementation.
- `wikipedia_search_server.py` - MCP server that returns Wikipedia summaries.
- `claude_wikipedia_search_server.py` - Claude-style Wikipedia server.
- `weather_forecast_client.py`, `wikipedia_search_client.py` - minimal example clients.
- `pyproject.toml` - project metadata / dependencies.

**Prerequisites**
- Python 3.10+ recommended.
- An OpenWeatherMap API key (set in `OPEN_WEATHER_API_KEY`).

**Setup**
1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (example):

```bash
pip install -r requirements.txt  # if you have one
# or install common deps directly
pip install fastmcp requests python-dotenv wikipedia uv
```

3. Create a `.env` file in the project root with your OpenWeatherMap key:

```text
OPEN_WEATHER_API_KEY=your_api_key_here
```

**Run servers**
The project uses simple entry scripts. You can run them with the `uv` runner that you used in this workspace, or with plain Python if you prefer.

Examples (matching how you've run them locally):

```bash
uv run wikipedia_search_server.py
uv run claude_weather_forecast_server.py
uv run weather_forecast_server.py
```

Or with Python directly:

```bash
python wikipedia_search_server.py
python claude_weather_forecast_server.py
```

**Run clients**

```bash
python weather_forecast_client.py
python wikipedia_search_client.py
```

**Environment & notes**
- The weather servers read `OPEN_WEATHER_API_KEY` from environment (dotenv is used in the scripts).
- `wikipedia_search_server.py` uses the `wikipedia` package to return `wikipedia.summary(search)`.
- Servers are small examples intended for learning MCP-style tool wrapping; they are not hardened for production.

**Next steps / suggestions**
- Add a `requirements.txt` or pin dependencies in `pyproject.toml`.
- Add README examples showing sample JSON responses and code snippets for calling the MCP endpoints.
- Add tests or a tiny demo script that calls each server tool.

---
If you'd like, I can also:
- add example `.env.example`,
- create `requirements.txt` from the current environment, or
- add usage examples that call the MCP endpoints programmatically.

