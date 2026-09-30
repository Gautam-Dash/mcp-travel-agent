from mcp_use import MCPClient
import asyncio


async def main():
    client = MCPClient.from_config_file(
        "playwright_mcp.json",
        code_mode=True
    )

    await client.create_all_sessions()

    print("Servers:", client.get_server_names())

    result = await client.execute_code("""
page = await playwright.browser_navigate(
    url="https://www.google.com"
)

return page
""")

    print("\nRESULT:")
    print(result)

    await client.close_all_sessions()


asyncio.run(main())