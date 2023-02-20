def print_fibonacci(num):
    n1, n2 = 0, 1
    count = 0
    if num <= 0:
        print('there is no fibonacci')
    elif num == 1:
        print(num)
    else:
        while count < num:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


if __name__ == '__main__':
    print_fibonacci(13)
