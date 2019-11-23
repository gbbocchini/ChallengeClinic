from django.shortcuts import render
from django.views import View
from django.conf import settings
import aiohttp
import asyncio
import uvloop
from .data_helpers.get_api_data import get_data
from .data_helpers.data_processor import DataProcessor

# asyncio "Booster"
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


class HomeView(View):
    def __init__(self, **kwargs):
        self.url = "https://api.openweathermap.org/data/2.5/forecast?id=3451328&appid="+settings.WEATHER_API_KEY
        self.data_processor = DataProcessor()
        super().__init__(**kwargs)

    def get(self, request):
        try:
            # calling the api in an async job, the process only goes on with a response
            response = loop.run_until_complete(get_data(self.url))
            dates = self.data_processor.response_processor(response)

            # single dates (the api returns results for 3 hours periods along 5 days, here get only single dates)
            date_format = self.data_processor.dates_processor(dates)

            # converting dates to week days
            weekday_format = self.data_processor.weekdays_processor(date_format)

            return render(
                request, "home.html", {"week_day": weekday_format, "date": date_format}
            )  # render dates and week days
        except RuntimeError:
            return render(
                request,
                "home.html",
                {
                    "error": "Ops, algo de errado nao esta certo! Tente outra vez por favor (F5)!"
                },
            )
