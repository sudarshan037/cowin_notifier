import json
import logging

from src.caller import district_caller
from src.messenger import send_message_list
from src.munger import data_parser


def runner(district_ids, user_details):
    timers = {pincode: {} for pincode in user_details.keys()}
    while True:
        district_data = {}
        for district_id in district_ids.values():
            # pprint(data_parser(district_caller(district_id)))
            district_data[district_id] = data_parser(district_caller(district_id))
            for pincode in district_data[district_id]:
                try:
                    timers = send_message_list(user_details[str(pincode)],
                                               district_data[district_id][pincode],
                                               timers)
                except KeyError:
                    continue
        # break


if __name__ == '__main__':
    logging.basicConfig(filename='logs/main.log',
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("start")
    with open('data/districts.json', 'r') as district_file:
        districts = json.load(district_file)
    with open('data/users.json', 'r') as user_file:
        users = json.load(user_file)
    runner(districts, users)
