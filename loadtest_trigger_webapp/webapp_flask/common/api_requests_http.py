import json

import requests


def postCall_without_auth(endpoint, requestBody, headers=None):
    response = requests.post(endpoint, json=requestBody, headers=headers)
    try:
        assert (response.status_code == 200)
        print("Status Code:" + str(response.status_code))
        print("Response:" + response.text)
    except AssertionError:
        print("API CALL FAILED for endpoint:" + endpoint)
        print("STATUS CODE:" + str(response.status_code))
        print("RESPONSE TEXT:" + response.text)
        print("RESPONSE HEADERS:" + json.dumps(dict(response.headers)))
    return response
