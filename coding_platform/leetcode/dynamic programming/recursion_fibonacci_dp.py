"""Fibonacci"""

"""calculate fibonacci number based position
0,1,1,2,3,5,8,13,21....
e.g.: n=5, then fib_num is 5
      n=8, then fib_num is 21
"""


def fibonacci_tail(n: int, a=0, b=1):
    # base case for fibonacci number is the first two numbers 0 and 1.
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail(n - 1, b, a + b)


"""The initial values are a=0 and b=1 (we can set the default values in Python). 
This is how we can use tail recursion to find Fibonacci-numbers!

Note that in this case there is just a single recursive function call which means that it is a faster approach - 
no need for two very similar recursive function calls (fibonacci_head(n-1) and fibonacci_head(n-2)). 
Python will not recalculate the same values several times."""


def fibonacci_head(n: int):
    # base case for fibonacci number is the first two numbers 0 and 1.
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib1 = fibonacci_head(n - 1)
    fib2 = fibonacci_head(n - 2)

    fib_num = fib1 + fib2
    return fib_num


""" here we will have multiple stack frames with same value as we are doing two recursive calls
that's why later on we will use dynamic programming to eradicate same value frames from stack memory
"""


# print the N-th Fibonacci number
def fibonacci_iteration(n):
    # these are the initial variables with initial values
    a, b = 0, 1

    while (n > 0):
        n = n - 1
        a, b = b, a+b
    return a


if __name__ == '__main__':
    print(fibonacci_head(8))
    print(fibonacci_tail(8))
    print(fibonacci_iteration(8))
