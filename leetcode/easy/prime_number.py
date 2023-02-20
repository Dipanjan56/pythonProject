import math


def check_prime(num: int) -> bool:
    if num == 0 or num == 1 or num / 2 == 0:
        return False
    elif num == 2:
        return True
    else:
        for i in range(3, int(math.sqrt(num)), 2):
            if num % i == 0:
                return False
    return True


if __name__ == '__main__':
    num = 247
    print(check_prime(num))
