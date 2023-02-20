def first_unique_character(s: str) -> str:
    count_dict = {}
    for char in s:
        if char not in count_dict.keys():
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    for i in range(len(s)):
        char = s[i]
        if count_dict[char] == 1:
            return char
    return f'No unique char in {s}'


if __name__ == '__main__':
    s = 'hello, hyderabad'
    print('first unique character: ', first_unique_character(s))
