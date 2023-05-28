import json
import random

from locust import SequentialTaskSet, task

from locust_project.common import api_request_locust
from locust_project.endpoints.endpoints import *
from locust_project.utilities.log_util import Logger
from locust_project.utilities.util_helper import UtilHelper


class Task2_Custom(SequentialTaskSet):
    header = {}
    id_list = []
    author_record = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.log_message('Entering into Task file')

    @task
    def get_author_record(self):
        endpoint = get_author_record_endpoint()
        resp = api_request_locust.get(self, endpoint, self.header)
        resp_json = resp.json()

        for record in resp_json:
            self.id_list.append(record.get('id'))


    # @task
    # def create_author_record(self):
    #     endpoint = create_author_record_endpoint()
    #     payload = {
    #         "id": UtilHelper.get_random_number(10000, 20000),
    #         "idBook": UtilHelper.get_random_number(10000, 20000),
    #         "firstName": f"Dipanjan{UtilHelper.get_random_number(0, 100)}",
    #         "lastName": "Kundu"
    #     }
    #     resp = api_request_locust.post(self, endpoint, self.header, payload)
    #     print(f'create_author_record Response: {resp.json()}')
    #
    # @task
    # def get_author_record_by_id(self):
    #     id = random.choice(self.id_list)
    #     endpoint = get_author_record_by_id_endpoint(id)
    #     resp = api_request_locust.get(self, endpoint, self.header)
    #     print(f'get_author_record_by_id Response: {resp.json()}')
    #     self.author_record = resp.json()
    #
    #
    #
    # @task
    # def update_author_record(self):
    #     id = random.choice(self.id_list)
    #     endpoint = update_author_record_endpoint(id)
    #     payload = self.author_record
    #     print(f'author_record: {payload}')
    #     resp = api_request_locust.put(self, endpoint, self.header, payload)
    #     print(f'update_author_record Response: {resp.json()}')
    #
    # @task
    # def delete_author_record(self):
    #     id = random.choice(self.id_list)
    #     endpoint = delete_author_record_endpoint(id)
    #     resp = api_request_locust.delete(self, endpoint, self.header)
    #     print(f'delete_author_record Response: {resp.content}')

    # @task
    # def exit_task_execution(self):
    #     UtilHelper.stop_locust_process(self)
