from config import uri, payload, headers
import requests
import json
from helpers import debug_save_to_json_request_and_response
import pytest


def test_send_request_goods_item_search():
    good_ids = ["3079071", "3079072", "3079073"]
    for id in good_ids:
        url = uri + '/goodsItemSearch'
        payload['Body']["Id"] = id

        response = requests.post(url, data=json.dumps(payload, indent=4), headers=headers)
        debug_save_to_json_request_and_response(payload=payload, response=response, test_purpose=id)
