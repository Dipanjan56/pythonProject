"""RECURSION Theory"""

"""
1. RECURSION is a method where the solution to a problem depends on solution to smaller instances of the same problem
   so we break the tasks into smaller and smaller subtasks
2. we have to define base-cases to avoid infinite loops
3. the recursive function calls and values are stored in stack memory

3. There are two types of recursion:
    Tail Recursion: if the recursion function call occurs at the end of the function then its called TAIL RECURSION
                    tail recursion is similar to loop (for or while)
                    this method executes all the statements before jumping to the next recursive call
                    
    Head Recursion: if the recursion function call occurs at the beginning of the function then its called HEAD RECURSION
                    This approach saves the state of the function call before jumping into the next recursive call
                    It means that head recursion needs more memory because of the states it stores 
                    

QnA:

1. WHY RECURSION CALLS ARE SLOWER THAN ITERATIVE CALLS?

Ans: Recursion is at least twice slower because first we unfold recursive calls(pushing them on a stack) until 
we reach the base case and then we traverse the stack and retrieve all recursive calls  

EXAMPLE: recursion_sum(4) -> 
In Stack:
    recursion_sum(4)
    recursion_sum(3)
    recursion_sum(2)
    recursion_sum(1)
    return 1
    return 2+1
    return 3+2+1
    return 4+3+2+1   
    
    
    
2. WHY WE GENERALLY TRY TO AVOID HEAD RECURSION?

Answer: For Head recursion, we use too many frames in the stack and hence there can be stack overflow 
and there is no room for function calls    



3. WHY IS IT POSSIBLE TO USE TAIL RECURSION OPTIMIZATION?

Ans: Because there is a fundamental difference between head recursion and tail recursion.

tail recursion related function calls (and the stack frames) do not depend on each other - 
there is no so-called "downward dependence" in the stack memory regarding the stack frames

head recursion related function calls DO depend on each other - they use values returned from other function calls
This is exactly why we can optimise tail recursion because the function calls and stack frames are totally independent of each other. 
                                  
"""


def tail_recursion(n):
    print(f'calling tail with n={n}')
    """base case"""
    if n == 0:
        return

    # do something
    print(n)

    # recursive call
    tail_recursion(n - 1)


""" it will give an output like this -> 5,4,3,2,1"""


# -------------------------------------------------------------------

def head_recursion(n):
    print(f'calling head with n={n}')
    """base case"""
    if n == 0:
        return

    # recursive call
    head_recursion(n - 1)

    # do something
    print(n)


""" it will give an output like this -> 1,2,3,4,5 -> because it will save the states of the function and at the end
it will print all of the remembered states"""

# -------------------------------------------------------------------


"""Calculate the sum of the first N integers"""


# with iterative approach
def sum_iteration(n: int) -> int:
    result = 0
    for num in range(n + 1):
        result += num
    return result


# with tail recursion
def sum_recursion(n: int) -> int:
    """we have to define a base case to avoid infinite loop"""
    if n == 0:
        return 0
    """now implement teh recursion"""
    return n + sum_recursion(n - 1)


# -------------------------------------------------------------------

"""Calculate factorial of a given number"""


# tail recursion
def factorial_recursion(n: int):
    if n == 1:
        return 1
    return n * factorial_recursion(n - 1)


def factorial_recursion_optimized(n: int, result: int):
    if n == 1:
        return result
    return factorial_recursion_optimized(n - 1, n * result)


"""in this case after the tail recursion, function call to the frame on the stack os no longer used(no unknown variables)
and it will finished with all the computation
"""

# -------------------------------------------------------------------


if __name__ == '__main__':
    print('tail recursion')
    tail_recursion(5)
    print('-----------------')
    print('head recursion')
    head_recursion(5)
    print('-----------------')
    print(sum_iteration(10))
    print(sum_recursion(10))
    print(factorial_recursion(5))
    print(factorial_recursion_optimized(5, 1))
