from random import random

from locust import SequentialTaskSet, task

from locust_project.common import api_requests


class PetStoreTasks(SequentialTaskSet):
    headers = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = {'accept': 'application/json'}
        self.status = 'available'
        self.pet_type = 'dog'
        self.pet_name = 'maria'
        self.tags = ''

    @task
    def get_pet_status(self):
        endpoint = '/pet/findByStatus?status=' + self.status
        api_requests.get(self, endpoint, self.headers)

    @task
    def add_new_pet(self):
        endpoint = '/pet'
        new_headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = {
            "id": 10,
            "category": {
                "id": 0,
                "name": self.pet_type
            },
            "name": self.pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": self.tags
                }
            ],
            "status": self.status
        }
        api_requests.post(self, endpoint, new_headers, payload)
