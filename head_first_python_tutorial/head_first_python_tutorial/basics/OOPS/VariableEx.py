"""Method & Variables"""

"""
3 types of Methods / functions

1. Instance Method - Use to access instance variable of the class
2. Class Method - Use to access static of the class
3. Static Method - Standalone method


"""


class Dog:
    """This are called as static/class level variable"""
    legs = 4

    def __init__(self):
        """This are called as instance variable"""
        self.name = "Milo"
        self.color = "Brown"

    """this is instance method"""
    def getDogName(self):
        print(self.name)

    @classmethod
    def getLegsCount(cls):
        print(cls.legs)

    @staticmethod
    def generalInformation():
        print("Beware of Dogs")


d1 = Dog()
d2 = Dog()

d2.name = "Bruno"
d2.color = "White"

Dog.legs = 3

print(d1.name, d1.color, Dog.legs)
d1.getDogName()
Dog.getLegsCount()

Dog.generalInformation()

print(d2.name, d2.color, Dog.legs)
