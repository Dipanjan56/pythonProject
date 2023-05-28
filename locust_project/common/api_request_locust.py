from locust.exception import RescheduleTask
from locust_project.utilities.log_util import *


def get(self, endpoint, headers, name=None):
    with self.client.get(endpoint, headers=headers, name=name, catch_response=True) as response:
        return check_response_code('GET', endpoint, response)


def post(self, endpoint, headers, request_body, name=None):
    with self.client.post(endpoint, headers=headers, json=request_body, name=name,
                          catch_response=True) as response:
        return check_response_code('POST', endpoint, response, request_body)


def put(self, endpoint, headers, request_body, name=None):
    with self.client.put(endpoint, headers=headers, json=request_body, name=name,
                         catch_response=True) as response:
        return check_response_code('POST', endpoint, response, request_body)


def delete(self, endpoint, headers, name=None):
    with self.client.delete(endpoint, headers=headers, name=name, catch_response=True) as response:
        return check_response_code('DELETE', endpoint, response)


def check_response_code(request_type, endpoint, response, request_body=None):
    if response.status_code == 200:

        if request_body is not None:
            Logger.log_message(
                '{} API Call request_body for endpoint {} : {}'.format(endpoint, request_type, request_body))
        Logger.log_message('{} API Call Successful for endpoint: {}'.format(request_type, endpoint))
        Logger.log_message(
            'Response headers of success for endpoint {} {} : {}'.format(request_type, endpoint, response.headers))
        Logger.log_message('Response for endpoint {} {} : {}'.format(request_type, endpoint, response.text))

        return response
    else:
        if request_body is not None:
            Logger.log_message(
                '{} API Call request_body for endpoint {}: {}'.format(endpoint, request_type, request_body),
                LogType.ERROR)
        Logger.log_message(
            '{} API Call Failed for endpoint: {} with code: {}'.format(request_type, endpoint,
                                                                       response.status_code),
            LogType.ERROR)
        Logger.log_message(
            'Response content of failure for endpoint {} {}: {}'.format(request_type, endpoint, response.content),
            LogType.ERROR)
        Logger.log_message(
            'Response headers of failure for endpoint {} {}: {}'.format(request_type, endpoint, response.headers),
            LogType.ERROR)
        Logger.log_message('Response for endpoint {} {} : {}'.format(request_type, endpoint, response.text),
                           LogType.ERROR)

        response.failure(f"API Call Failed | Status Code: {response.status_code}")
        raise RescheduleTask()
