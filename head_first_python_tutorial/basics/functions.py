import functools


def add(x, y):
    return x + y


def reverse(text):
    return text[::-1]


def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


# if we want some default parameters so that if we dont give any still function should run
# default parameters must go at the end
def about1(name, age, likes="Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


# multiple default parameters
def about2(name, age=23, likes="Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


# all default parameters
def about3(name="Dk", age=23, likes="Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


def unpack_arguments():
    numbers = [1, 2, 3, 4]
    print(numbers)
    print(*numbers)  # unpacking of numbers
    print("abc")
    print(*"abc")
    print("a", "b", "c")


# packing number works as var args in java i.e. we can give any number of arguments here
# it is very useful when we dont know actually how many number of arguments gonna come
def pack_arguments(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


# unpack a dictionary : use **
def unpack_dictionary():
    dictionary = {"name": "DK", "age": 19, "likes": "python"}
    print(about(**dictionary))


# pack a dictionary : use **
def pack_dictionary(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


def convert_char_to_ascii():
    char = 'A'
    ascii_value = ord(char)
    print(ascii_value)


def convert_ascii_to_char():
    ascii_value = 65
    char = chr(ascii_value)
    print(char)


def fsdf(x):
    return x % 2 != 0


# using lambda and filter function
def filter_function_print_odd():
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
    odd_numbers = list(filter(fsdf, li))
    print(odd_numbers)


# using map function
# get square value of all the elements in a list
def map_function():
    li = [1, 2, 3, 4, 5, 6]
    square_values = list(map(lambda x: x * x, li))
    print(square_values)
    len(li)


def reduce_function():
    # initializing list
    lis = [1, 3, 5, 6, 2]

    # using reduce to compute sum of list
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(lambda a, b: a + b, lis))

    # using reduce to compute maximum element from list
    print("The maximum element of the list is : ", end="")
    print(functools.reduce(lambda a, b: a if a > b else b, lis))

    lis_2 = ['a', 'ab', 'abc', 'abcd']
    print("The maximum length string of the list_2 is : ", end="")
    print(functools.reduce(lambda a, b: a if len(a) > len(b) else b, lis_2))


# using zip function
def zip_functions():
    name = ["a", "b", "c", "d"]
    roll_no = [1, 2, 3, 4]
    marks = [70, 85, 97, 63]

    # using zip() to map values and returning as a list
    mapped = list(zip(name, roll_no, marks))
    print(mapped)


# using zip and forloop
def zip_for_loop():
    players = ["Sachin", "Shewag", "Ganguly", "Dhoni"]
    scores = [80, 65, 78, 52]

    # printing players and score
    for player, score in zip(players, scores):
        print("{} scored {}".format(player, score))


def something():
    nums1 = [1, 2, 3, 0, 0, 0]
    for i in range(3, len(nums1)):
        nums1.pop()


if __name__ == '__main__':
    # print(add(5, 10))
    # print(reverse("hello"))
    # print(reverse([1, 2, 3, 4]))
    # print(about("Dk", 27, "FIFA 21"))  # these are positional arguments
    # print(about(age=27, name="Dk", likes="FIFA 21"))  # these are keyword arguments
    # print(about1("Dk", 27))  # use of Default parameters
    # print(about2("Dk"))  # use of multiple default parameters
    # print(about3())
    # print(about3(name="Dipanjan", likes="Football"))
    # unpack_arguments()
    # print(pack_arguments(2, 3))
    # print(pack_arguments(11, 22, 33, 44))
    # unpack_dictionary()
    # pack_dictionary(penny="Female", dk="male")
    # print_odd()
    # map_function()
    # zip_functions()
    # zip_for_loop()
    reduce_function()
    # something()
