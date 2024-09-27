import math


def check_prime(num: int) -> bool:
    if num == 2:
        return True
    if num == 0 or num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = 2
    print(check_prime(num))
