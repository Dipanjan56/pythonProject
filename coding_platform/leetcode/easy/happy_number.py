""""""
from typing import List

"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false


"""


def is_happy(n: int) -> bool:
    while n > 3:
        n2 = 0
        while n > 0:
            if n2 == n:
                return False
            n1 = n // 10
            n2 += (n % 10) ** 2
            n = n1
        n = n2

    if n == 1:
        return True
    else:
        return False


def is_happy_2(n: int) -> bool:
    def get_next_number(num):
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit ** 2
            num //= 10
        return total_sum

    seen_numbers = set()  # This set keeps track of numbers we have already processed

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)  # Add the number to the set of seen numbers
        n = get_next_number(n)  # Replace n by the sum of the squares of its digits

    # After the loop exits, we check whether n is 1
    return n == 1  # If n is 1, return True (n is a happy number), otherwise return False


if __name__ == '__main__':
    n = 4
    print(is_happy(n))
    print(is_happy_2(n))
