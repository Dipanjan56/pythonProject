"""

Inheritance:


Class A ---> Base Class  / Parent Class - Single level Inheritance

    def add(self):

Class B ---> Derived Class / Child Class


so from Inheritance we can access members, properties and methods from the another class

A <--- B <--- C - MultiLevel Inheritance

A    B --> Multiple Inheritance

  C

in multiple inheritance, diamond problem does not occur as it follows the order at which the parent classes are inherited
"""


class AnimalParent:
    def a(self):
        print("I am inside AnimalParent class")

    def ap(self):
        print("Inside the Animal Parent class")

    def hello(self):
        print("Hello from Animal Parent class")


class Animal:
    name = "Rahul"

    def a(self):
        print("I am inside Animal class")

    def hello(self):
        print("Hello from Animal class")


class Mamals(AnimalParent, Animal):
    def b(self):
        print("I am inside Mamals class")


if __name__ == '__main__':
    mam = Mamals()
    mam.b()
    mam.a()
    print(mam.name)
    mam.ap()
    mam.hello()
