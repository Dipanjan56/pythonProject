"""FACTORIAL"""
"""Calculate factorial of a given number"""

"""tail recursion"""


def factorial_tail(n: int):
    # this is the base case - 0! = 1
    if n == 1:
        return 1
    return n * factorial_tail(n - 1)


def factorial_tail_optimized(n: int, accumulator: int = 1):
    if n == 1:
        return accumulator
    return factorial_tail_optimized(n - 1, n * accumulator)


"""in this case after the tail recursion, function call to the frame on the stack os no longer used(no unknown variables)
and it will finished with all the computation

n=5, acc = 1
n=4, acc = 5
n=3, acc = 20
n=2, acc = 60
n=1, acc = 120
So, the dependency is contained in the accumulator, hence there is no requirement of backtracking
in tail recursion, stack frames are fully independent on each other
"""

# -----------------------------------------------------------------------

"""head recursion"""


def factorial_head(n):
    # this is the base case - 0! = 1
    if n == 1:
        return 1

    # use recursion: store the sub_results in multiple frames
    sub_result = factorial_head(n - 1)

    # do some operation: calculate the factorial using those frame results
    result = n * sub_result
    return result


"""in head recursion, stack frames are heavily dependent on each other and there must be backtracking"""

if __name__ == '__main__':
    print(factorial_tail(5))
    print(factorial_tail_optimized(5, 1))
    print(factorial_head(5))
