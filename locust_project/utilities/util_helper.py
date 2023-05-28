import csv
import os
import random
from locust.exception import StopUser
from locust_project.utilities.log_util import Logger


class UtilHelper:
    user_list = []

    @staticmethod
    def get_random_number(start, end):
        number = random.randint(start, end)
        return number

    @staticmethod
    def stop_locust_process(self):
        if "RUN_TIME" in os.environ:
            self.interrupt()
        else:
            print(f'Currently running user count [after completion]: {self.user.environment.runner.user_count}')
            Logger.log_message(
                f'Currently running user count [after completion]: {self.user.environment.runner.user_count}')
            if self.user.environment.runner.user_count == 1:
                self.user.environment.runner.quit()
            raise StopUser()

    @staticmethod
    def load_users(csv_file_path):
        reader = csv.DictReader(open(csv_file_path))
        for line_elem in reader:
            UtilHelper.user_list.append(line_elem)

    @staticmethod
    def get_user():
        if len(UtilHelper.user_list) < 1:
            UtilHelper.load_users('test_credentials.csv')
        user_obj = UtilHelper.user_list.pop()
        return user_obj
