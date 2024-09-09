from locust import events, HttpUser

from locust_project.taskset import PetStoreTasks

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("LOAD TEST STARTED........")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("LOAD TEST COMPLETED")

class TestPetStore(HttpUser):
    tasks = [PetStoreTasks]


'''
To run this file, enter this command: 

locust --config ./locust_project/config/pet_store_demo.conf 
'''