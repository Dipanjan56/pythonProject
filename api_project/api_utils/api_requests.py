import json

import requests

def get(host: str, endpoint: str, headers=None, cookies=None):
    url = host + endpoint
    response = requests.get(url=url, headers=headers, cookies=cookies)
    resp_json = validate_response(url, 'GET', response)
    return resp_json

def post(host: str, endpoint: str, payload: json, headers=None, cookies=None):
    url = host + endpoint
    response = requests.post(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = validate_response(url, 'POST',response)
    return resp_json

def put(host: str, endpoint: str, payload: json, headers=None, cookies=None):
    url = host + endpoint
    response = requests.post(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = validate_response(url, 'PUT', response)
    return resp_json

def delete(host: str, endpoint: str, headers=None, cookies=None):
    url = host + endpoint
    response = requests.get(url=url, headers=headers, cookies=cookies)
    resp_json = validate_response(url, 'DELETE', response)
    return resp_json


def validate_response(url, type, response):
    try:
        assert (response.status_code == 200)
        print(f'\n{type} API CALL IS SUCCESSFUL FOR URL: {url}')
        print(f'RESPONSE TEXT: {response.text}')
        print(f'RESPONSE HEADER: {json.dumps(dict(response.headers))}')
    except AssertionError:
        print(f'\n{type} API CALL IS FAILED FOR URL: {url}')
        print(f'STATUS CODE: {response.status_code}')
        print(f'RESPONSE TEXT: {response.text}')
        print(f'RESPONSE HEADER: {json.dumps(dict(response.headers))}')
        raise Exception(f'{type} API CALL IS FAILED FOR URL: {url}')
    return response.json()