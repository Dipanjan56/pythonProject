# functions: take some line of code , give them a name and you 've got a function.
# function is initialised by  keyword 'def some_name():'
# function introduce two new keyword: 'def' and 'return'
# function can accept argument
# function contain code and usually documentation

# module: take a collection of function and package them as a file and you've got a module

# standard library: collection of modules

# we can define the type of argument and return type by using annotations
# e.g def function_name(parameter: type) -> return type:
# function annotations are optional

# -----------------------------------------

# example:
from datetime import date

date_today = date.today()
print(date_today)


# here datetime: standard library, date: module, today(): function

# -----------------------------------------
# create your own function

def convert_number_to_string(n):
    """converting a integer to string"""
    return str(n)


# -----------------------------------------

# invoking a function

print(convert_number_to_string(5))


# -----------------------------------------

# example: identify vowels in string

def search_vowels(word):
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search_vowels('hello'))
print(search_vowels('sky'))


# -----------------------------------------

# example: if vowels in string then true otherwise false

def search_vowels_2(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


print(search_vowels_2('hello'))
print(search_vowels_2('sky'))

# -----------------------------------------

# we can define the type of argument and return type by using annotations
# e.g def function_name(parameter: type) -> return type:

def search_vowels_3(word: str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_vowels_4(word: str) -> bool:
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

# -----------------------------------------
