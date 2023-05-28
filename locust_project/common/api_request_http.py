import requests
import json
from locust_project.utilities.log_util import Logger, LogType


def get(host: str, endpoint: str, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.get(url=url, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def post(host: str, endpoint: str, payload: json, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.post(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def put(host: str, endpoint: str, payload: json, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.put(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def delete(host: str, endpoint: str, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.delete(url=url, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def check_response_status_code(url, response):
    try:
        assert (response.status_code == 200)
        Logger.log_message("API CALL SUCCESSFUL for endpoint:" + url)
        Logger.log_message("RESPONSE TEXT:" + response.text)
        Logger.log_message("RESPONSE HEADERS:" + json.dumps(dict(response.headers)))
    except AssertionError:
        Logger.log_message("API CALL FAILED for url:" + url, LogType.ERROR)
        Logger.log_message("STATUS CODE:" + str(response.status_code), LogType.ERROR)
        Logger.log_message("RESPONSE TEXT:" + response.text, LogType.ERROR)
        Logger.log_message("RESPONSE HEADERS:" + json.dumps(dict(response.headers)), LogType.ERROR)
        raise Exception("API CALL FAILED for url:" + url, LogType.ERROR)
    return response.json()

