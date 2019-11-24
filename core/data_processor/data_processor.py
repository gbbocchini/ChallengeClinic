import json
from datetime import datetime


class Processor(object):
    @staticmethod
    def forecast_response_processor(response):
        data = json.loads(response)["list"]

        # dict with only dates + humidity data
        temp_dict = {
            "date": [data[i]["dt_txt"] for i in range(len(data))],
            "humidity": [data[i]["main"]["humidity"] for i in range(len(data))],
        }

        # based on the dict above, filter only dates with humidity >= 70
        result_dict = {
            "date": [
                temp_dict["date"][i].split(" ")
                for i in range(len(temp_dict["date"]))
                if temp_dict["humidity"][i] >= 70
            ]
        }
        dates = [result_dict["date"][i][0] for i in range(len(result_dict["date"]))]
        return dates

    @staticmethod
    def forecast_dates_processor(dates):
        final = []
        for i in dates:
            if i not in final:
                final.append(i)
        return final

    @staticmethod
    def forecast_weekdays_processor(final):
        result = []
        for i in final:
            result.append(datetime.strptime(i, "%Y-%m-%d").strftime("%A"))
        return result

    @staticmethod
    def weathernow_response_processor(response):
        data = json.loads(response)["main"]
        return data
