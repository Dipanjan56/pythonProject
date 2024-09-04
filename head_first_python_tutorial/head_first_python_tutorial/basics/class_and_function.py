# self is an alias to the object [like 'this' keyword in java]
# dunder '__' provide hooks into every class's standard behavior
# object class is parent class to all the classes in python
# hence all the dunder methods provided by objects are available to your classes to use or overwrite it,
# all these dunder method are known as 'magic method'
# all functions are objects and they have unique id

class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr


if __name__ == '__main__':
    h = CountFromBy(100, 10)
    print(h.val)
    print(h.incr)
    h.increase()
    print(h.val)
    print(h)

    g = CountFromBy()
    print(g.val)
    print(g.incr)
    g.increase()
    print(g.val)
    print(g)
