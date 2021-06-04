import random
import time
from datetime import date
from json import JSONDecodeError
from pprint import pprint

from requests import get

user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
]
today = date.today()
date = today.strftime("%d-%m-%Y")


def district_caller(district_id):
    headers = {
        "User-Agent": user_agents[random.randint(0, 1)]}
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
    params = {
        'district_id': district_id,
        'date': date
    }
    r = get(url=url, params=params, headers=headers)
    time.sleep(2)
    try:
        data = r.json()
    except JSONDecodeError:
        data = {"centers": []}
        print("60 second sleep")
        time.sleep(60)
    return data


def pincode_caller(pincode):
    headers = {
        "User-Agent": user_agents[random.randint(0, 1)]}
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'
    params = {
        'pincode': pincode,
        'date': today.strftime("%d-%m-%Y")
    }
    r = get(url=url, params=params, headers=headers)
    time.sleep(1)
    try:
        data = r.json()
    except JSONDecodeError:
        data = {"centers": []}
        print("60 second sleep")
        time.sleep(60)
    return data


if __name__ == "__main__":
    # pprint(district_caller('523'))
    # pprint(pincode_caller('311001'))
    from munger import data_parser
    pprint(data_parser(pincode_caller('311022')))
    # pprint(data_parser(district_caller('523')))
