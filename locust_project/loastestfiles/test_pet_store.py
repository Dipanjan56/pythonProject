from locust import HttpUser, between, events

from locust_project.taskset.pet_store_tasks import PetStoreTasks

@events.test_start.add_listener
def on_start(environment, **kwargs):
    print("LOAD TEST STARTED........")

@events.test_stop.add_listener
def on_stop(environment, **kwargs):
    print("LOAD TEST COMPLETED")

class TestPetStore(HttpUser):
    wait_time = between(0.2, 1)
    tasks = [PetStoreTasks]


'''
To run this file, enter this command: 

locust --config ./locust_project/config/pet_store_demo.conf 
'''