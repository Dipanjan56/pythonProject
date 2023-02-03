"""
Function Decorator: It adjusts the behavior of an existing function without changing the function's original code
It means, decorator allows you to take some existing code and augment it with additional behavior if needed
Decorator can be applied to classes an functions, although they are mainly applied to functions and primarily called
as 'function decorators'
# function decorator is always prefixed with @, e.g: @app.route('/').

How to create a decorator:
1. create a function
2. pass a function as an argument to a function
3. return function from a function
4. process any number and type function arguments

Recipe of Decorator:
1. A decorator is a function, which manipulates an existing function
2. A decorator takes the decorated function as an argument
3. A decorator returns a new function
4. A decorator maintains the decorated function's signature

Decorator Template: See decorator_template.py in basics folder
AND
see example in checker.py in webapp_flask directory and it usage in simple_webapp_using_decorator.py

"""

#################################################################

'''Item 2 - pass a function as an argument to a function'''


def apply(func: object, value: object) -> object:
    return func(value)


apply(print, 42)
print(apply(type, 42))
print(apply(id, 42))

#################################################################

'''Item 3 - return function from a function'''

'''before that we need to know about nested function'''


def outer():
    def inner():
        print('This is inner')

    print('this is outer, invoking inner.')
    inner()


outer()

# --------------------------------------------------------

'''Now return a function from a function'''


def outer():
    def inner():
        print('This is inner')

    print('this is outer, returning inner.')
    return inner


i = outer()
i()

#################################################################

'''Item 4 - process any number and type function arguments'''

""" 1.Use * to accept any number of arguments e.g. def func(*args) """


def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


"""Here < print(a, end=' ')> is used like this to print all teh arg values in a single line"""

myfunc(10)
myfunc()
myfunc(10, 20, 30, 40)
values = [1, 2, 3, 4, 5]
myfunc(values)

""" myfunc(values) -> it will return like this -> [1, 2, 3, 4, 5]
But if you want to instruct the interpreter to expand the list to behave 
as if each of the list's were an individual argument, prefix the list's
name with * character when invoking the function -> myfunc(*values)
"""

myfunc(*values)

# --------------------------------------------------------

""" 2.Use ** to accept any arbitrary keyword argument e.g. def func(**kwargs) """


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


myfunc2(a=10, b=20)
myfunc2()
myfunc2(a=10, b=20, c=30, d=40, e=50)
dbconfig = {'host': '127.0.0.1',
            'user': 'myUserid',
            'password': 'myPassword',
            'database': 'myDB'}
myfunc2(**dbconfig)

"""by **, we tell the interpreter to treat the single dictionary as a collection of keys and their associated values """

""" 3.Accepting any number and type of function arguments"""


def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


myfunc3()
myfunc3(1, 2, 3)
myfunc3(4, 5, 6, a=10, b=20, c=30)
#################################################################
