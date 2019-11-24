from django.test import SimpleTestCase, Client
from django.conf import settings
import asyncio
import uvloop
import requests
import json

from .repository.get_api_data import ApiHandler
from .data_processor.data_processor import Processor
from .views import HomeView

home = HomeView()
processor = Processor()
api_handler = ApiHandler()

urlForecast = (
    "https://api.openweathermap.org/data/2.5/forecast?id=6322515&appid="
    + settings.WEATHER_API_KEY
)
urlWeather = (
    "https://api.openweathermap.org/data/2.5/weather?id=6322515&appid="
    + settings.WEATHER_API_KEY
)


response_forecast0 = api_handler.get_forecast()
data_forecast0 = json.loads(response_forecast0)["list"]

response_forecast1 = requests.get(urlForecast)
data_forecast1 = response_forecast1.json()["list"]

response_weather0 = api_handler.get_weather_now()
data_weather0 = json.loads(response_weather0)["main"]

response_weather1 = requests.get(urlWeather)
data_weather1 = response_weather1.json()["main"]

c = Client()
response_get = c.get("/")
response_post = c.post("/")


class TestApiHandler(SimpleTestCase):
    def test_urls(self):
        self.assertEqual(api_handler.urlForecast, urlForecast)
        self.assertEqual(api_handler.urlWeatherNow, urlWeather)
        print("Tested Api url to be called", flush=True)

    def test_retrieve(self):
        self.assertEqual(data_forecast0, data_forecast1)
        self.assertEqual(data_weather0, data_weather1)
        print("Tested api data retrieve", flush=True)


class HomeViewTestCase(SimpleTestCase):
    def test_response_200(self):
        self.assertEqual(response_get.status_code, 200)
        print("Tested response 200", flush=True)

    def test_response_405(self):
        self.assertEqual(response_post.status_code, 405)
        print("Tested response 400", flush=True)

    def test_template(self):
        self.assertTemplateUsed(response_get, "home.html")
        print("Tested Template usage", flush=True)
