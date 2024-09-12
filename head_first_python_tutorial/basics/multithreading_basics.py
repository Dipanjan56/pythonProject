""""""
"""
Threading:
To use concurrency we use threading

if a func invokes a func and wait for that func to invoke and lets say the second function takes 30 sec wait
but we do not want to wait and want to execute next code block, we use thread


1. Multithreading in Python

	•	Multithreading involves running multiple threads (smaller units of a process) concurrently within a single process.
	•	Threads share the same memory space, which allows them to easily share data but also introduces the possibility
	 of race conditions and data inconsistencies if not managed properly.

In Python, multithreading is often limited by the Global Interpreter Lock (GIL), which is a mutex that allows only one
 thread to execute Python bytecode at a time. This means multithreading in Python is best suited for I/O-bound tasks 
 (like waiting for data from an external source), rather than CPU-bound tasks (like heavy computations).

When to Use Multithreading:

	•	Best suited for tasks that involve a lot of waiting or I/O operations, such as:
	•	Web scraping
	•	Reading/writing files
	•	Network requests
	•	Not ideal for CPU-intensive tasks due to the GIL.
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


if __name__ == '__main__':
    do_some_work()
