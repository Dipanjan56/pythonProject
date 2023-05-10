"""
Threading:
To use concurrency we use threading

if a func invokes a func and wait for that func to invoke and lets say the second function takes 30 sec wait
but we do not want to wait and want to execute next code block, we use thread
"""

from threading import Thread
from time import sleep



def do_some_work():
    t = Thread(target=execute_slowely, args=(10, 20, 30))
    t.start()
    print('executing next block immediately without waiting for execute_slowely function to complete')


def execute_slowely(a, b, c):
    sleep(10)
    print(a, b, c)


do_some_work()
