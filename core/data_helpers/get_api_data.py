import aiohttp
import asyncio


async def get_data(url):
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            await client.close()
            return await response.text()



