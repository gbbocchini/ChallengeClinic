from django.shortcuts import render
from django.views import View
import aiohttp
import asyncio
import uvloop
import json
from datetime import datetime
from .helpers.get_api_data import get_data

# asyncio "Booster"
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


class HomeView(View):
    @staticmethod
    def get(request):
        try:
            # calling the api in an async job, the process only goes on with a response
            response = loop.run_until_complete(get_data())
            data = json.loads(response)["list"]

            # dict with only dates + humidity data
            temp_dict = {
                "date": [data[i]["dt_txt"] for i in range(len(data))],
                "humidity": [data[i]["main"]["humidity"] for i in range(len(data))],
            }

            # based on the dict above, filter only dates with humidity => 70
            result_dict = {
                "date": [
                    temp_dict["date"][i].split(" ")
                    for i in range(len(temp_dict["date"]))
                    if temp_dict["humidity"][i] >= 70
                ]
            }
            dates = [result_dict["date"][i][0] for i in range(len(result_dict["date"]))]

            # single dates (the api returns results for 3 hours periods along 5 days, here get only single dates)
            final = []
            for i in dates:
                if i not in final:
                    final.append(i)

            # converting dates to week days
            result = []
            for i in final:
                result.append(datetime.strptime(i, "%Y-%m-%d").strftime("%A"))
            return render(
                request, "home.html", {"week_day": result, "date": final}
            )  # render dates and week days
        except RuntimeError:
            return render(
                request,
                "home.html",
                {
                    "error": "Ops, algo de errado nao esta certo! Tente outra vez por favor (F5)!"
                },
            )
