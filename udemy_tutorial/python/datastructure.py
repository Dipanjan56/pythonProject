import random


def lists():
    # Initialise empty list
    l1 = []
    l2 = list()
    print(type(l1), type(l2))
    # Initialise list with values
    list1 = [2, 7, 9, 5, 0]
    print(list1)
    print(type(list1))

    # a list single list can contain all kind of data type
    list2 = ["A", "B", "C", 1, 2, 3, True, False]
    print(list2)
    print(type(list2[0]))
    print(type(list2[4]))
    print(type(list2[6]))

    # slicing a list : basic slice format is : variable[start(inclusive):end(exclusive):step(toSkip)]
    # [exactly same as string slicing]
    # print first 3 characters
    print(list2[:3])
    print(list2[0:3])
    print(list2[0:3:1])

    list3 = [1, 2, [3, 4, 5], 6, 7, 8]
    # get the list inside the list
    print(list3[2])
    # get the number 3
    print(list3[2][0])

    # create a table : list inside a list
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # get8
    print(table[2][1])

    # get length of a list
    print(len(list3))

    # remove a value from a list : it will remove the first occurrence only
    list4 = [2, 7, 9, 5, 0, 7]
    list4.remove(7)
    print(list4)

    # remove a specific index
    list5 = [2, 7, 9, 5, 0]
    del list5[0]
    print(list5)

    # remove first 3 elements of a list
    list6 = [2, 7, 9, 5, 0]
    del list6[0:3]
    print(list6)

    # add element in a list
    list7 = [1, 2, 3, 4]
    list7.append(5)
    print(list7)

    # list concatenation : only a list can be added with list
    list8 = [1, 2]
    list9 = [3, 4]
    list8 = list8 + list9
    print(list8)
    list8 = list8 + [5]
    print(list8)
    list8 = list8 + ["A"]
    print(list8)
    list8 = list8 + list("B")
    print(list8)
    # same thing cant be done on integer as integer is iterable so it cant be converted to list using list method
    # work around
    list8 = list8 + list(str(6))
    print(list8)

    # add a list inside a list
    list8 = list8 + [[7, 8, 9]]
    list8.append([10, 11, 12])
    # never do like this : list8 = list.append(11) as append returns empty value
    print(list8)

    # get the last index or the list that added inside the list
    print(list8[-1])

    # insert a number in between : variable.insert[position,number] : position means where you want to insert
    list10 = [1, 2, 4, 5]
    list10.insert(2, 3)
    # never do like this : list8 = list.insert(2,3) as insert returns empty value
    print(list10)

    A, B, C = [1, 2, 3]
    print(A)
    print(B)
    print(C)

    # reverse a list
    list12 = [1, 2, 3, 4]
    print(list12[::-1])

    # select 3 random values from a list[it can be duplicate]
    list13 = [1, 2, 3, 4]
    print(random.choices(list13, k=3))

    # select unique random values from a list
    list14 = [1, 2, 3, 4]
    print(random.sample(list14, k=3))


def tuples():
    # Its immutable data type, works similar as list : used for storing a=data for the first time and read operation
    # use this if we want to protect the stored data and dont want the data to be changed accidentally
    # Initialise empty tuple
    t1 = ()
    t2 = tuple()
    print(type(t1), type(t2))
    # Initialise tuple with values
    # tuple1 = 1, 2, 3, "A", "B", "C"
    tuple1 = (1, 2, 3, "A", "B", "C")
    print(tuple1)
    print(type(tuple1))

    # Slicing a tuple : basic slice format is : variable[start(inclusive):end(exclusive):step(toSkip)]
    # get first 3 element from tuple
    print(tuple1[:3])

    # change a list to tuple
    list11 = [1, 2, 3]
    print(tuple(list11))

    # assign multiple variable in tuple
    (A, B, C) = 1, 2, 3
    print(A)
    print(B)
    print(C)


def dictionaries():
    # create an empty dictionary
    d = dict()
    print(type(d))
    students = {}
    students = {"Alice": 25, "Bob": 27, "Claire": 29, "Dan": 21, "Emma": 22}
    print(students)

    # get a particular value
    print(students["Dan"])

    # add another key value in dictionary
    students["Fred"] = 25
    print(students)

    # change a value to a key
    students["Alice"] = 26
    print(students)

    # remove a key
    del students["Fred"]
    print(students)

    # print all teh keys from a dictionary
    print(students.keys())  # this is dict_keys data type which is not iterable and ot doesn't support indexing

    # iterate over the keys
    list_key = list(students.keys())
    print(list_key)
    print(list_key[2])

    # print all the values from a dictionary
    print(students.values())  # this is dict_values data type which is not iterable and ot doesn't support indexing

    # iterate over the keys
    list_value = list(students.values())
    print(list_value)
    print(list_value[2])

    # get all the items from a dictionary
    print(students.items())

    # iterate over dictionaries
    for key, value in students.items():
        print(key)
        print(value)

    # store multiple values in a key
    students = {"Alice": ["ID001", 26, "A"],
                "Bob": ["ID002", 27, "B"],
                "Claire": ["ID003", 29, "C"],
                "Dan": ["ID004", 21, "D"],
                "Emma": ["ID005", 22, "E"],
                }
    print(students)

    # slicing a dictionary

    # get id of Bob
    print(students["Bob"][0])

    # get age and grade of Dan
    print(students["Dan"][1:])

    # store a dictionary in dictionary
    students = {"Alice": {"id": "ID001", "age": 26, "grade": "A"},
                "Bob": {"id": "ID002", "age": 27, "grade": "B"},
                "Claire": {"id": "ID003", "age": 29, "grade": "C"},
                "Dan": {"id": "ID0014", "age": 21, "grade": "D"},
                "Emma": {"id": "ID005", "age": 22, "grade": "E"},
                }
    print(students)

    # get grade of Emma
    print(students["Emma"]["grade"])

    # get age and id of Claire
    print(students["Claire"]["age"], students["Claire"]["id"])


def sets():
    #: set stores only unique values : set is unordered and un-indexed
    # Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

    # Initialise empty set
    empty_set = set()
    print(type(empty_set))

    # initialise set with values
    s = {"a", "b", "c", "a"}
    print(s)

    # adding an element to the set
    s.add(1)
    print(s)

    # removing an element
    s.remove("b")
    print(s)

    # iterate over set
    for val in s:
        print(val)

    # 2: Iterating over a set using enumerated for loop.

    # Creating a set using string
    test_set = set("geEks")

    # Iterating using enumerated for loop
    for id, val in enumerate(test_set):
        print(id, val)


def frozen_sets():
    # Frozen sets in Python are immutable objects that only support methods and operators
    # that produce a result without affecting the frozen set or sets to which they are applied.
    # While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
    # If no parameters are passed, it returns an empty frozenset.

    # Initialise a empty frozen set
    empty_frozen_set = frozenset()
    print(type(empty_frozen_set))

    # Initialise frozen set with values
    f_set = frozenset({1, 2, 3})
    print(f_set)

    # iterate over frozen set
    for val in f_set:
        print(val)


if __name__ == '__main__':
    # lists()
    # tuples()
    # dictionaries()
    sets()
    frozen_sets()

