"""String Encode and Decode"""
from typing import List

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""


def encode(strs: List[str]) -> str:
    """
    Encodes a list of strings to a single string.
    """
    # Encode each string with its length followed by a '#'
    encoded_string = ''.join(f'{len(s)}#{s}' for s in strs)
    return encoded_string


def decode(s: str) -> List[str]:
    """
    Decodes a single string to a list of strings.
    """
    decoded_list = []
    i = 0

    while i < len(s):
        # Find the position of the next '#'
        j = s.find('#', i)
        # Get the length of the next string (prefix before '#')
        length = int(s[i:j])
        # Extract the string of length `length` following the '#'
        decoded_list.append(s[j + 1:j + 1 + length])
        # Move the pointer `i` to the next part of the encoded string
        i = j + 1 + length
    return decoded_list

def check_encode_decode(strs: List[str]) -> bool:
    if strs == decode(encode(strs)):
        print(decode(encode(strs)))
        return True
    return False


if __name__ == '__main__':
    strs = ["neet","code","love","you"]
    print(check_encode_decode(strs))