""""""
from typing import List

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45

"""


def climb_stairs_recursion(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)


memo = {}


def climb_stairs_memo(n: int) -> int:
    if n in memo.keys():
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)
    return memo[n]


def climb_stairs_bottom_up(n: int) -> int:
    if n == 1:
        return 1
    dp = [-1] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    n = 5
    print(climb_stairs_recursion(n))
    print(climb_stairs_memo(n))
    print(climb_stairs_bottom_up(n))
