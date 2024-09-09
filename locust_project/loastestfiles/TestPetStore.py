from locust import HttpUser, between

from locust_project.taskset import PetStoreTasks

def on_start(self):
    print("LOAD TEST STARTED........")

def on_stop(environment, **kwargs):
    print("LOAD TEST COMPLETED")

class TestPetStore(HttpUser):
    wait_time = between(0.2, 1)
    tasks = [PetStoreTasks]


'''
To run this file, enter this command: 

locust --config ./locust_project/config/pet_store_demo.conf 
'''