from django.test import SimpleTestCase
from django.test import Client, client
from django.conf import settings
import asyncio
import uvloop
import requests
import json

from .helpers.get_api_data import get_data, url
from .views import HomeView


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()

urlTest = "https://api.openweathermap.org/data/2.5/forecast?id=3451328&appid="+settings.WEATHER_API_KEY

response0 = loop.run_until_complete(get_data())
data0 = json.loads(response0)['list']

request = requests.get(urlTest)
data1 = request.json()['list']

c = Client()
response_get = c.get('/')
response_post = c.post('/')


class GetDataTestCase(SimpleTestCase):
    def test_url(self):
        self.assertEqual(urlTest, url)
        print("Tested Urls", flush=True)

    def test_retrieve(self):
        self.assertEqual(data0, data1)
        print("Tested api data retrieve", flush=True)


class HomeViewTestCase(SimpleTestCase):
    def test_response_200(self):
        self.assertEqual(response_get.status_code, 200)
        print("Tested response 200", flush=True)

    def test_response_405(self):
        self.assertEqual(response_post.status_code, 405)
        print("Tested response 400", flush=True)

    def test_template(self):
        self.assertTemplateUsed(response_get, 'home.html')
        print("Tested Template usage", flush=True)







