def while_loops():
    # print 1 to 10 skipping 5 using pass/continue : both will work
    n = 1
    while n <= 10:
        if n == 5:
            n = n + 1
            pass
        else:
            print(n)
            n = n + 1

    # print even numbers from 10 till 20
    m = 10
    while m <= 20:
        if m % 2 == 0:
            print(m)
        m = m + 1

    # add names in list till the size becomes 3
    L = []
    while len(L) < 3:
        new_name = input("Please add new name: ").strip().capitalize()
        L.append(new_name)
    print("Sorry the list is full")
    print(L)


def for__lops():
    # print 1 to 10 : use range function : it gives a range iterable in python 3 : syntax = range(start{inclusive},stop{exclusive},step)
    for number in range(1, 11):
        print(number)

    # print numbers skipping one at a time from 1 to 10
    for number in range(1, 11, 2):
        print(number)

    # iterate through list
    for number in [1, 2, 3, 4]:
        print(number)

    # print all characters of a string using iteration
    for letter in "abcd":
        print(letter)

    # print numbers vowels and constants present in  a letter
    vowels = 0
    constants = 0

    for letter in "Hello":
        if letter.lower() in "aeiou":
            vowels = vowels + 1
        elif letter == " ":
            pass
        else:
            constants = constants + 1
    print("vowels: {}".format(vowels))
    print("constants: {}".format(constants))

    # iterate through dictionaries and print those names who has "a" in the name
    students = {"male": ["Tom", "Harry", "John"],
                "female": ["Clara", "Penny", "Ammy"]
                }

    for key in students.keys():
        for name in students[key]:
            if "a" in name.lower():
                print(name)

    # list comprehension
    # print even numbers
    even_numbers = [x for x in range(1, 10) if x % 2 == 0]
    print(even_numbers)
    # print odd numbers
    odd_numbers = [x for x in range(1, 10) if x % 2 != 0]
    print(odd_numbers)

    words = ["the", "quick", "brown", "fox"]
    answer = [[w.upper(), w.lower(), len(w)] for w in words]
    print(answer)


if __name__ == '__main__':
    # while_loops()
    for__lops()
