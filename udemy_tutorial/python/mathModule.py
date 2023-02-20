import math


def mathFunctions():
    # rounding off tp nearest integer using built in function
    x = round(2.7)
    print(round(2.7))

    # rounding off to nearest lesser number[forcefully] using math library
    x = math.floor(2.7)
    print(x)

    # rounding off to nearest bigger number[forcefully] using math library
    x = math.ceil(2.2)
    print(x)

    # print pi value
    x = math.pi
    print(x)

    # print e value
    x = math.e
    print(x)

    # get hypotenuse of a triangle
    x = math.hypot(3, 4)
    print(x)

    # get 2^3 i.e 8
    x = math.pow(2, 3)
    print(x)

    # get 2^3 i.e 8 [shortcut] [integer form]
    x = 2 ** 3
    print(x)

    # get exponential of any number
    x = math.exp(2)
    print(x)

    # get log e of a number
    x = math.log(math.e)
    print(x)

    # get log 10 of a number
    x = math.log10(1000)
    print(x)


if __name__ == '__main__':
    mathFunctions()
