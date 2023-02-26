""""""
"""
Public: by default all the functions and variables are public

Protected:  we need to add this '_' ->  eg.  _var, def _method()

Private: we need to add this '__' -> eg.: __var, def __method()


"""

class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car constructor")

    def publicMethod(self):
        print("Calling public method")


    def _protectedMethod(self):
        print("Calling protected method")



    def __privateMethod(self):
        print("Calling private method")


if __name__ == '__main__':
    car = Car()
    print(car.publicVar)
    """python wont give you auto suggestion for protected variable although you can still acccess it outside the class"""
    print(car._protectedVar)
    # print(car.__privateVar) # it will give you error
    """but if you want to still access the private variable you have to specify '_ClassName' like this below"""
    print(car._Car__privateVar)

    car.publicMethod()
    car._protectedMethod()
    car.__privateMethod()