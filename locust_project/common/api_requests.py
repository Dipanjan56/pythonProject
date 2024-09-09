from locust.exception import RescheduleTask


def get(self, endpoint, headers, name=None):
    with self.client.get(endpoint, headers = headers, name=name, catch_response=True) as response:
        return check_response_code('GET', endpoint, response)

def post(self, endpoint, headers, request_body, name=None):
    with self.client.post(endpoint, headers=headers, json=request_body, name=name, catch_response=True) as response:
        return check_response_code('POST', endpoint, response)



def check_response_code(request_type, endpoint, response):
    if response.status_code == 200 or response.status_code == 201 or response.status_code == 202:
        print(f'{request_type} API call is successful for this endpoint {endpoint}')
        print(f'Response for the endpoint {request_type} {endpoint}: {response.text}')
    else:
        print(f'{request_type} API call is failure for this endpoint {endpoint}')
        print(f'Response for the endpoint {request_type} {endpoint}: {response.content}')
        response.failure('API Failed')
        raise RescheduleTask()

    return response