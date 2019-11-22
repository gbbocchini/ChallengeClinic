import aiohttp
import asyncio
from django.conf import settings


url = "https://api.openweathermap.org/data/2.5/forecast?id=3451328&appid="+settings.WEATHER_API_KEY


async def get_data():
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            await client.close()
            return await response.text()
