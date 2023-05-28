from locust import events
from locust import between
from locust import HttpUser

from locust_project.taskset.task1 import Task1
from locust_project.utilities.log_util import Logger


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ..........")
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    Logger.log_message("......... Initiating Load Test ..........")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message('Load Test Completed')
    print('Load Test Completed')


class test_apis(HttpUser):
    wait_time = between(0.2, 1)
    tasks = [Task1]