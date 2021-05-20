import configparser
from datetime import datetime
from pprint import pprint

import pytz
from telethon import TelegramClient


class User:
    api_id, api_hash, phone, username = (None, None, None, None)
    client = None

    def __init__(self):
        # Reading configs
        config = configparser.ConfigParser()
        config.read("config.ini")

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
            result))
    pprint(result)


def send_message_list(users, result):
    for center_id in result.keys():
        for user in users:
            print("send_message:", user, result[center_id])


if __name__ == "__main__":
    send_message('me', 'blah')
