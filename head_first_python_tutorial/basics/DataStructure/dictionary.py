# Dictionary id used to hold key/value pairs
# empty dictionary is initialised by CURLY BRACES: {}

# the key part of dictionary is typically a string and the value part can be any Python object
# but keys and values dont have to be strings forever

# In dictionary, insertion order is not maintained, so Unlike lists, which keep your objects arranged in the order
# in which you inserted them, dictionary does not.

# you have to initialise dictionary like this:  dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} so that we can use this
# key value in runtime but there is a method 'setdefault()' which ease our initialisation at runtime
# setdefault(): setdefault()'s usage guarantees that a key is always initialised to a starter value at runtime and
# any possibility of 'KeyError' exception is avoided and
# you never need to spend time initialising all your rows of dictionary data ahead of time

# you can print the complex dictionary output in pretty format using pprint module

import pprint

# -----------------------------------------

# Initialise a dictionary with values
person1 = {'Name': 'Dipanjan', 'Gender': 'Male', 'Occupation': 'SDET', 'Planet': 'Earth'}

print(person1)

# Initialise empty dictionary
# method 1
empty_dict = {}

# method 2
empty_dict2 = dict()

# -----------------------------------------

# add key-value in a dict

person1['Address'] = 'Pune'

# -----------------------------------------

# delete key-value in a dict

person1.pop('Address')

# -------------------------------

# access values associated with the keys by using square bracket []
value = person1['Name']
print(f'access values according to the keys: {value}')

# -----------------------------------------

# add key/value pair in dictionary

person1['Age'] = 33
print(f'Dictioanry after adding key/value pair: {person1}')

# -----------------------------------------

# Iterate over a dictionary with keys and values

print('\nIterate over a dictionary with keys and values: \n')
for key, value in person1.items():
    print(f'\t{key} : {value}')

# -----------------------------------------

# Iterate over a dictionary with keys only

print('\nIterate over a dictionary with keys only: \n')
for key in person1.keys():
    value = person1[key]
    print(f'\t{key} : {value}')

# -----------------------------------------

# Iterate over a dictionary with values only

print('\nIterate over a dictionary with values only: \n')
for value in person1.values():
    print('\t', value)

# -----------------------------------------

# example: find the number of vowels present in the word

# 1st way: initialising only a dictionary with key, value
word = 'Hitchhiker'
found = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for k in found.keys():
    letter = k
    for char in word:
        if letter == char:
            found[k] += 1

print('find the number of vowels present in the word [1st way]: ', found)

# 2nd way: using list and initialising empty dictionary and using 'in' or 'not in' condition
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Hitchhiker'
found = {}

for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 0
        found[letter] += 1

print('find the number of vowels present in the word [2nd way]: ', found)

# 3rd way: using list and initialising empty dictionary and using 'setdefault' condition

vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Hitchhiker'
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

print('find the number of vowels present in the word [3nd way]: ', found)

# -----------------------------------------

# Sort a dictionary: use 'sorted()' function,  but it will give you the sorted list of keys

letter_dict = {'c': 2, 'a': 1, 'e': 5, 'd': 7, 'b': 4}
print(f'\nletter_dict before sorting: {letter_dict}')

print(f'\nletter_dict after sorting [1st way]:')
for key in sorted(letter_dict):
    value = letter_dict[key]
    print(f'\t{key} : {value}')

print(f'\nletter_dict after sorting [2nd way]:')
for key, value in sorted(letter_dict.items()):
    print(f'\t{key} : {value}')

# print in sorted descending order of keys
print(sorted(letter_dict.items(), reverse=True))

# print in sorted descending order of values
print(sorted(letter_dict.items(), key=lambda x: x[1], reverse=True))

# -----------------------------------------

# pretty printing dictionary

person1 = {'Name': 'Dipanjan', 'Gender': 'Male', 'Occupation': 'SDET', 'Planet': 'Earth'}
person2 = {'Name': 'Namrata', 'Gender': 'FeMale', 'Occupation': 'HR', 'Planet': 'Earth'}

person_dict = {'Dipanjan': person1, 'Namrata': person2}

print('pretty printing of dictionary: \n')
pprint.pprint(person_dict)
