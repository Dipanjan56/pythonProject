# global variable
a = 100
l = [1, 2, 3]


def f1():
    a = 50
    print(a)
    # local variable
    b = 200
    print(b)


def f2():
    a = 90
    print(a)


def f3():
    # override global variable inside a function
    global a
    a = 20
    print(a)


def f4():
    l = 10000
    print(l)


def f5():
    l[0] = 9
    # for list and dictionaries if we change the elements of the global list in a function,
    # it will actually affect the global list variable and change the element in global variable itself
    print(l)


if __name__ == '__main__':
    f1()
    f2()
    print(a)
    f3()
    print(a)
    f4()
    print(l)
    f5()
    print(l)

    # python will not change the global variable value inside function scope, global variable will remain same
    # instead it will create another local variable with same name in the function scope
    # once function run finishes python will automatically remove local variable from memory
    # But, for list and dictionaries if we change the elements of the global list in a function,
    # it will actually affect the global list variable and change the element in global variable itself
