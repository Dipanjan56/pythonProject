def first_unique_character(s: str) -> str:
    count_dict = {}
    for char in s:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1

    """as order of dictionary is not maintained thats why we are iterating over the string again to get the key value in orederly format"""
    for char in s:
        if count_dict[char] == 1:
            print(char)
            return char
    return f'No unique char in {s}'


if __name__ == '__main__':
    s = 'hello, hyderabad'
    print('first unique character: ', first_unique_character(s))
