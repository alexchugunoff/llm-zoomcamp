from fastmcp import Client
import asyncio
import mcp_server

async def main():
    async with Client(mcp_server.mcp) as mcp_client:        
        result = await mcp_client.call_tool("get_weather", {"city": "berlin"})
        return result

if __name__ == "__main__":
    test = asyncio.run(main())
    print(test)