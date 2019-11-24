from django.shortcuts import render
from django.views import View
from django.conf import settings
from .data_processor.data_processor import Processor
from .repository.get_api_data import ApiHandler


class HomeView(View):
    def __init__(self, **kwargs):
        self.processor = Processor()
        self.api_handler = ApiHandler()
        super().__init__(**kwargs)

    def get(self, request):
        try:
            # calling the api for 5 day forecast (async func)
            response = self.api_handler.get_forecast()
            dates_raw = self.processor.forecast_response_processor(response)

            # single dates (the api returns results for 3 hours periods along 5 days, here get only single dates)
            date_format = self.processor.forecast_dates_processor(dates_raw)

            # converting dates to week days
            weekday_format = self.processor.forecast_weekdays_processor(date_format)

            # getting weather now
            response_weather_now = self.api_handler.get_weather_now()
            data_weather_now = self.processor.weathernow_response_processor(
                response_weather_now
            )

            temp_now = data_weather_now["temp"] // 10
            humidity_now = data_weather_now["humidity"]

            # render results
            return render(
                request,
                "home.html",
                {
                    "week_day": weekday_format,
                    "date": date_format,
                    "temp_now": temp_now,
                    "hum_now": humidity_now,
                },
            )
        except RuntimeError:
            return render(
                request,
                "home.html",
                {
                    "error": "Ops, algo de errado nao esta certo! Tente outra vez por favor (F5)!"
                },
            )
