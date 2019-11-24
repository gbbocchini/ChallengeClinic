import aiohttp
import asyncio
import uvloop
from django.conf import settings

# asyncio "Booster"
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


async def get_data(url):
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            await client.close()
            return await response.text()


class ApiHandler(object):
    def __init__(self):
        self.urlForecast = (
            "https://api.openweathermap.org/data/2.5/forecast?id=6322515&appid="
            + settings.WEATHER_API_KEY
        )
        self.urlWeatherNow = (
            "https://api.openweathermap.org/data/2.5/weather?id=6322515&appid="
            + settings.WEATHER_API_KEY
        )

    def get_forecast(self):
        response = loop.run_until_complete(get_data(self.urlForecast))
        return response

    def get_weather_now(self):
        response = loop.run_until_complete(get_data(self.urlWeatherNow))
        return response
