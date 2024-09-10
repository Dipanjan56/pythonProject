"""Euclidean Algorithm"""

"""Euclidean Algorithm, is an efficient method for computing the Greatest Common Divisor [GCD] of two integers -
the largest number that divides them both without a reminder

e.g. GCD(45, 10) = 5
    
    algo:
    for two given numbers a & b such that a>=b:
        if a mod b == 0 then GCD(a,b) = b
        else GCD(a,b) = GCD(b, a mod b)
        
        eg. GCD(24, 9) ->
            24 mod 9 = 6
            now GCD(9,6) ->
            9 mod 6 = 3
            now GCD(6, 3) ->
            6 mod 3 = 0 
            end of algorithm 
            
            So, GCD(24, 9) = 3
"""


# tail recursion
def gcd_recursion(a, b):
    # base case: if a % b = 0 i.e. no reminder, then b is gcd
    if a >= b:
        if a % b == 0:
            return b

    return gcd_recursion(b, a % b)


def gcd_iteration(a, b):
    if a >= b:
        if a % b == 0:
            return b

    while a % b != 0:
        a, b = b, a % b

    return b


if __name__ == '__main__':
    print(gcd_recursion(24, 9))
    print(gcd_iteration(24, 9))
