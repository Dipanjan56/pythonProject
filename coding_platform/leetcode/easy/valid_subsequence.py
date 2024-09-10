"""is subsequence"""

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

"""
In this approach, I am using two pointers and if pointer matches I am slicing the list t from the immediate next of 
where the pointer matches and also creating list having the matching element, so that when next char in s comes we 
already slices the list from the match pointer

if the the list having the matching element and ans the string s matches then its true
"""
def is_subsequence(s: str, t: str) -> bool:

    l = []
    for char in s:
        for i in range(len(t)):
            if t[i] == char:
                l.append(t[i])
                t = t[i + 1:]
                break

    subsequence_s = ''.join(l)

    if s == subsequence_s:
        return True
    return False


def is_subsequence_optimized(s: str, t: str) -> bool:
    # Initialize two pointers
    s_pointer, t_pointer = 0, 0

    # Iterate through both strings
    while s_pointer < len(s) and t_pointer < len(t):
        # If characters match, move the s_pointer
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        # Always move the t_pointer
        t_pointer += 1

    # If we've gone through all characters in s, it's a subsequence
    return s_pointer == len(s)


# Example usage:
s1 = "abc"
t1 = "ahbgdc"
result1 = is_subsequence(s1, t1)
print(result1)  # Output: True

s2 = "axc"
t2 = "ahbgdc"
result2 = is_subsequence(s2, t2)
print(result2)  # Output: False


if __name__ == '__main__':
    s1 = "abc"
    t1 = "ahbgdc"
    print(is_subsequence(s1, t1))

    s2 = "ab"
    t2 = "baab"
    print(is_subsequence(s2, t2))
