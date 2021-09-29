from config import uri, payload, headers
import requests
import json
from helpers import debug_save_to_json_request_and_response
import pytest

def print_field_in_body_value(response, field_name=''):
    print(response['Body']['GoodsItemList'][0][field_name])
    print('\n')

#def check_goods_item_list_not_empty(response):
    #assert len(response['Body']['GoodsItemList']) !=0

# моя первая функция, проверка кол-ва товара в выдаче
def check_goods_item_list_not_empty_brand(response):
    goodsitemlist_count = len(response['Body']['GoodsItemList'])
    print(goodsitemlist_count)
    assert goodsitemlist_count !=0


# вторая моя функция, проверка строки TotalCount в боди
def print_field_in_body_value_total_count(response, field_name=''):
    assert field_name in response['Body'].keys()
    # print(response['Body'][field_name])
    # print('\n')

def test_send_request_goods_item_search():
    url = uri + '/goodsItemSearch'
    payload['Body']['GoodsCategoryId'] = "5526"

    response = requests.post(url, data=json.dumps(payload, indent=4), headers=headers)
    debug_save_to_json_request_and_response(payload=payload, response=response, test_purpose='test_serezha')

    print_field_in_body_value_total_count(response=response.json(), field_name='TotalCount')
    check_goods_item_list_not_empty_brand(response=response.json())
        
        