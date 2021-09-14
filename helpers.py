import json
from os import makedirs


def debug_save_to_json_request_and_response(payload, response, test_purpose):
    directory = './response_and_requests'
    makedirs(directory, exist_ok=True)
    file_name = test_purpose.replace('\n', '').replace('/', '_')
    with open(f'{directory}/{file_name}.json', 'a', encoding='utf-8') as json_file:
        json.dump(payload, json_file, ensure_ascii=False)
        json.dump(response.json(), json_file, ensure_ascii=False)
