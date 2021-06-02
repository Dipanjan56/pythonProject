def comparison_operator():
    a = True
    print(type(a))
    b = 2 < 3
    print(b)

    # if condition
    if True:
        print("It worked")

    # if-else condition
    num1 = 100
    num2 = 100

    if num1 > num2:
        print("num1 is bigger than num2")
    elif num2 > num1:
        print("num2 is bigger than num1")
    else:
        print("Both numbers are equal")


def logical_operator():
    # logical operator : NOT
    x = 10
    y = 20
    if not y < x:
        print("NOT: It worked")

    # logical operator : AND
    c = 10
    d = 5
    if c > 10 and d > 1:
        print("AND: It worked")
    else:
        print("AND: It didn't work")

    # logical operator : NAND [NOT + AND]
    if not (c > 10 and d > 1):
        print("NAND: It worked")
    else:
        print("NAND: It didn't work")

    # logical operator : OR
    if c > 10 or d > 1:
        print("OR: It worked")
    else:
        print("OR: It didn't work")

    # logical operator : NOR
    if not (c > 10 or d > 1):
        print("NOR: It worked")
    else:
        print("NOR: It didn't work")


if __name__ == '__main__':
    # comparison_operator()
    logical_operator()
