"""

Multiprocessing in Python

	•	Multiprocessing involves running multiple processes concurrently, where each process has its own memory space.
	•	Unlike multithreading, multiprocessing in Python does not have the GIL restriction, which makes it suitable for 
	CPU-bound tasks (such as complex calculations or data processing) where multiple CPU cores can be fully utilized.
	•	Each process runs independently with its own Python interpreter, memory, and resources, which means 
	they don’t share data directly.

When to Use Multiprocessing:

	•	Best suited for CPU-bound tasks such as:
	•	Data processing
	•	Mathematical computations
	•	Machine learning training
	•	Ideal when you need to take advantage of multiple cores in modern CPUs to perform tasks faster.


Let us try to understand the below code:

To import the multiprocessing module, we do:
import multiprocessing

To create a process, we create an object of Process class. It takes following arguments:
target: the function to be executed by process
args: the arguments to be passed to the target function
Note: Process constructor takes many other arguments also which will be discussed later. 
In above example, we created 2 processes with different target functions:

p1 = multiprocessing.Process(target=print_square, args=(10, ))
p2 = multiprocessing.Process(target=print_cube, args=(10, ))
To start a process, we use start method of Process class.
p1.start()
p2.start()

Once the processes start, the current program also keeps on executing. 
In order to stop execution of current program until a process is complete, we use join method.
p1.join()
p2.join()

As a result, the current program will first wait for the completion of p1 and then p2. 
Once, they are completed, the next statements of current program are executed.
"""

import multiprocessing
import time


def print_cube(num):
    """
    function to print cube of given num
    """
    time.sleep(5)
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    time.sleep(10)
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")
