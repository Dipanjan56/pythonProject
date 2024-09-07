"""Swagger Petstore"""
import random

from api_project.api_utils import api_requests

"""
Link: https://petstore.swagger.io/
"""

host = 'https://petstore.swagger.io/v2'
headers = {'accept': 'application/json'}


def get_pet_status(status: str):
    endpoint = '/pet/findByStatus?status=' + status
    api_requests.get(host, endpoint, headers)


def add_new_pet(pet_name: str, pet_type: str, tags: str, status: str):
    endpoint = '/pet'
    new_headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "id": random.randint(10000, 1000000),
        "category": {
            "id": 0,
            "name": pet_type
        },
        "name": pet_name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": tags
            }
        ],
        "status": status
    }
    resp_json = api_requests.post(host, endpoint, payload, new_headers)
    pet_id = resp_json.get('id')
    pet_type = resp_json.get('category').get('name')
    pet_name = resp_json.get('name')
    print(f'\nA new pet {pet_type} named {pet_name} has been added successfully, PET ID: {pet_id}')


if __name__ == '__main__':
    status = 'available'
    get_pet_status(status)
    add_new_pet('tom', 'dog', 'tom', status)
