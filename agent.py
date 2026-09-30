import os
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPClient

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

PLAYWRIGHT_CONFIG = BASE_DIR / "playwright_mcp.json"

playwright_client = None


def create_llm():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )


async def get_playwright_client():
    global playwright_client

    if playwright_client is None:
        playwright_client = MCPClient.from_config_file(
            str(PLAYWRIGHT_CONFIG),
            code_mode=True,
        )

        await playwright_client.create_all_sessions()

    return playwright_client


async def generate_response(user_input: str, tool_result: str):
    llm = create_llm()

    prompt = f"""
You are a helpful AI travel and web assistant.

User request:
{user_input}

Browser result:
{tool_result}

Give the user a natural, useful response.

Rules:
- Never mention MCP.
- Never mention Playwright.
- Never mention code execution.
- Never mention internal tools.
- Never show raw browser logs.
- Never say "Ran Playwright code".
- Never expose technical execution details.
- Answer the user's request directly.
"""

    response = await llm.ainvoke(prompt)

    return response.content


async def run_playwright(user_input: str):
    client = await get_playwright_client()

    text = user_input.lower().strip()

    if "open google" in text:

        query = None

        search_phrases = [
            "search for",
            "search",
            "look for",
            "find",
        ]

        for phrase in search_phrases:
            if phrase in text:
                index = text.find(phrase)
                query = user_input[index + len(phrase):].strip()
                break

        if query:
            encoded_query = quote_plus(query)

            url = f"https://www.google.com/search?q={encoded_query}"

        else:
            url = "https://www.google.com"

    elif text.startswith("open "):

        url = user_input[5:].strip()

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

    else:

        query = user_input.strip()

        encoded_query = quote_plus(query)

        url = f"https://www.google.com/search?q={encoded_query}"

    code = f"""
result = await playwright.browser_navigate(
    url="{url}"
)

return result
"""

    result = await client.execute_code(code)

    if result.get("error"):
        raise RuntimeError(result["error"])

    return await generate_response(
        user_input,
        result["result"],
    )


async def run_agent(user_input: str):
    return await run_playwright(user_input)


async def clear_memory():
    return None


async def close_agent():
    global playwright_client

    if playwright_client:
        await playwright_client.close_all_sessions()
        playwright_client = None