"""swap two number without using third variable"""


def swap_two_number(a1: int, a2: int):
    print(f'a1: {a2} | a1: {a1}')

    sum = a1 + a2
    a2 = sum - a2
    a1 = sum - a1
    print(f'a1: {a2} | a1: {a1}')


if __name__ == '__main__':
    a1 = 10
    a2 = 4
    swap_two_number(a1, a2)
