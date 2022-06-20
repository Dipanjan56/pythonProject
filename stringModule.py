def method():
    # broken string
    message = 'John said to me "I will see you later"'
    print(message)

    # multiLine sentence
    message = '''When they had sworn to this advised doom,
They did conclude to bear dead Lucrece thence;
To show her bleeding body thorough Rome,
And so to publish Tarquin’s foul offence:
Which being done with speedy diligence,
The Romans plausibly did give consent
To Tarquin’s everlasting banishment.'''
    print(message)

    # # take input from console
    # name = input("What is your Name?: ")
    # print(name)

    # concat two strings
    x = "part one"
    y = "part two"
    print(x + y)

    # concat string and integer using type casting
    x = "My age is: "
    y = 27
    print(x + str(y))

    # concat string and integer using format
    x = "My age is: {}"
    y = 27
    print(x.format(y))

    # concat string and integer using format with multiple values
    x = "I want to pay {1} for apple quantity {0} and my balance will be Rs. {2} after this"
    print(x.format(5, 30, 190))

    # concat string and print in single line
    print("I want to pay {1} for apple quantity {0} and my balance will be Rs. {2} after this".format(5, 30, 190))

    # get occurrence of characters in a string
    print("Hello World".count("o"))
    print("happy birthday".count("day"))

    # make upper case
    x = "Happy Birthday"
    print(x.lower())

    # make upper case
    x = "Happy Birthday"
    print(x.upper())

    # make first letter as upper case of a sentance
    x = "happy birthday"
    print(x.capitalize())

    # make first letter of each word as upper case
    x = "happy birthday"
    print(x.title())

    # check if a string contains only letters
    print(x.isalpha())
    # it will come as false as x contains a space and space is not letters

    # check if string contains only letters
    x = "123"
    print(x.isdigit())

    # check if string is alphaNumeric
    x = "abcd123"
    print(x.isalnum())

    # get index or starting position of a word in a sentence
    x = "hello world"
    print(x.index("world"))
    # but here if we give any substring which is not present, it will throw runtime error

    # get index of a word no matter if its present or not
    x = "hello world"
    print(x.find("world"))
    print(x.find("asd"))
    # in this case it wil print -1 as its not present

    # remove space in between
    x = "happy birthday"
    print(x.replace(" ", ""))

    # remove character
    x = " 000000happybirthday00000 "
    print(x.strip("0"))  # remove all 0's
    print(x.lstrip("0"))  # remove only left side 0's
    print(x.rstrip("0"))  # remove only right side 0's
    print(x.strip())  # remove white spaces from both the sides or trim it

    # get length of  a string
    print(len(x))

    # join a list of string to make a sentence
    list_strings = ["I", "am", "Dipanjan"]
    print(" ".join(list_strings))


def sliceString():
    # basic slice format is : variable[start(inclusive):end(exclusive):step(toSkip)]

    word = "ABCDEF123456"

    # get 0th index
    print(word[0])

    # get last index element
    print(word[-1])

    # get ABCDEF
    print(word[:6])
    print(word[0:6])
    print(word[0:6:1])
    print(word[word.index("ABCDEF"):word.index("123")])

    # get ACE
    print(word[0:6:2])

    # get 123456
    print(word[6:len(word)])
    print(word[6:])

    # reverse the whole string
    print(word[::-1])

    # Use negative indexes to start the slice from the end of the string:
    # print 345
    print(word[-4:-1])

    email = "dipanjan.kundu@mindtcikle.com"
    user = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print(user)
    print(domain)

    email = "dipanjan.kundu@mindtcikle.com"
    user = email.split('@')[0]
    domain = email.split('@')[1]
    print(user)
    print(domain)


if __name__ == '__main__':
    # method()
    # sliceString()
    x = "hello world"
    print(x.find("hello"))
