from config import uri, payload, headers
import requests
import json
from helpers import debug_save_to_json_request_and_response


def send_request_goodsItemSearch(uri, payload, headers):
    url = uri + '/goodsItemSearch'
    payload['Body']["Id"] = 3079071

    response = requests.post(url, data=json.dumps(payload, indent=4), headers=headers)
    debug_save_to_json_request_and_response(payload=payload, response=response, test_purpose='тест')


send_request(uri, payload, headers)
