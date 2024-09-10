""""""
from typing import List

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    bracket_stack = []

    for char in s:
        if char in bracket_dict.keys():
            bracket_stack.append(char)
        elif len(bracket_stack) == 0:
            return False
        else:
            last_open_bracket_from_stack = bracket_stack.pop()
            expected_closing_bracket = bracket_dict[last_open_bracket_from_stack]
            actual_closing_bracket = char
            if actual_closing_bracket != expected_closing_bracket:
                return False

    print(f'bracket_stack :{bracket_stack}')

    if len(bracket_stack) == 0:
        return True

    return False


if __name__ == '__main__':
    s = "([)]"
    print(is_valid(s))
