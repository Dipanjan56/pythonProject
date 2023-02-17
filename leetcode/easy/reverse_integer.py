def reverse_integer(num: int) -> int:
    rev_num = 0
    while num > 0:
        reminder = num % 10
        num = num // 10
        rev_num = (rev_num * 10) + reminder

    return rev_num


if __name__ == '__main__':
    num = 1234
    print(reverse_integer(num))
