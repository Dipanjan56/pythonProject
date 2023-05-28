from locust import events, LoadTestShape
from locust import between
from locust import HttpUser

from locust_project.taskset.task1_custom import Task2_Custom
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
    tasks = [Task2_Custom]


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 5, "users": 5, "spawn_rate": 5},
        {"duration": 10, "users": 30, "spawn_rate": 20},
        {"duration": 15, "users": 50, "spawn_rate": 25}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
