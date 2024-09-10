def print_fibonacci(num):
    a, b = 0, 1
    count = 0
    if num <= 0:
        print('there is no fibonacci')
    elif num == 1:
        print(num)
    else:
        while count < num:
            print(a)
            fib_num = a + b
            a = b
            b = fib_num
            count += 1


if __name__ == '__main__':
    print_fibonacci(13)
