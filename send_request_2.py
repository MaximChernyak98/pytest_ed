from config import uri, payload, headers
import requests
import json
from helpers import debug_save_to_json_request_and_response
import pytest


def test_send_request_goods_item_search():
    url = uri + '/goodsItemSearch'
    payload['Body']["Id"] = "3079071"

    response = requests.post(url, data=json.dumps(payload, indent=4), headers=headers)
    debug_save_to_json_request_and_response(payload=payload, response=response, test_purpose='тест3')


def test_send_request_delivery_info():
    url = uri + '/DeliveryInfo'
    payload['Body']

    response = requests.post(url, data=json.dumps(payload, indent=4), headers=headers)
    debug_save_to_json_request_and_response(payload=payload, response=response, test_purpose='тест4')

# test_send_request_goods_item_search()
test_send_request_delivery_info()
