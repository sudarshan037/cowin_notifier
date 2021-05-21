import configparser
import traceback
from datetime import datetime
from pprint import pprint
from time import time

import pytz
from telethon import TelegramClient


class User:
    api_id, api_hash, phone, username = (None, None, None, None)
    client = None

    def __init__(self):
        # Reading configs
        config = configparser.ConfigParser()
        config.read("src/config.ini")

        # setting config values
        self.api_id = config['Telegram']['api_id']
        self.api_hash = str(config['Telegram']['api_hash'])
        self.phone = config['Telegram']['phone']
        self.username = config['Telegram']['username']

    def set_client(self):
        # Create the client and connect
        # noinspection PyTypeChecker
        self.client = TelegramClient(
            self.username,
            self.api_id,
            self.api_hash
        )
        tz_India = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz_India)
        print(now.strftime("%d-%m-%Y"), "|", now.time(), ":Client Created")

    def get_client(self):
        return self.client


def send_message(username, result):
    user = User()
    user.set_client()
    client = user.get_client()
    with client:
        client.loop.run_until_complete(client.send_message(
            username,
            str(result)))
    pprint(result)


def tic(user, center_id, result, timers):
    try:
        return timers[str(result[center_id]['pincode'])][center_id][user]
    except KeyError as e:
        return e


def toc():
    return round(time(), 2)


def send_message_list(users, result, timers):
    for center_id in result.keys():
        pincode = str(result[center_id]['pincode'])
        try:
            if toc() - timers[pincode][center_id] > 600:
                timers[pincode][center_id] = toc()
                for user in users:
                    send_message(user, result[center_id])
                    print("send_message: Updated Timer", user, result[center_id])
        except KeyError:
            traceback.print_exc()
            timers[pincode][center_id] = toc()
            for user in users:
                send_message(user, result[center_id])
                print("send_message: Initialized Timer", user, result[center_id])
    return timers


if __name__ == "__main__":
    send_message('me', 'blah')
