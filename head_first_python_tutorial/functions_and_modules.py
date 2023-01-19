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

# also we can specify default values for arguments
# e.g def function_name(parameter: type=value) -> return type:
# this means function uses the default value if no value for the argument is provided

# there are two type: positional argument and keyword argument

# module: any file, which contains functions is called  module
# you just have to import the file using python's import statement

# there are three main locations interpreter searches when looking for a module
# 1. Current working directory[cwd]: the dir you are currently working in
# 2. Interpreter's site packages location: these are directory that contains any third party python module you may have
#    installed(including any written by you)
# 3. Standard library locations: these are th directory that contains all the modules that make up the standard library

# for any 'import module', interpreter first searches your cwd first.

# --------------------------------------------------------------------

# Getting Module into site-packages: Using 'setuptools'
# As a release of 3.4 of Python, standard lib includes a module called 'setuptools', which can be used to add any
# module to site-packages.
# Steps:
# 1. Create a distribution description: this identifies the module we want 'setuptools' to install: this step requires
#    us to create two descriptive files for our module: setup.py and readme.txt
# 2. Generate a distribution file: Using python at cmd, we will create a shareable distribution file to contain our
#    module's code
# 3. Install the distribution file: Again, using python at cmd, install the  distribution file into site-packages

# see example in module_to_site_packages folder
# Step1 description:
# setup.py file describes our module in some detail
# in addition to setup.py, the setuptools mechanism requires the existence of one another file - 'readme' file - into
# which you can put description of your package - README.txt

# Step2 description:
# cmd -> go to the module folder -> cd head_first_python_tutorial/module_to_site_packages/
# cmd -> python3 setup.py sdist [here sdist is passed as an argument] : sdist means it will create a folder 'dist
# and' in that folder it will combine all the 3 files and  into a source distribution file as a tarred archive file
# [ext: .tar.gz], which contains the source code for your module
# now you are ready to install your module into site-packages

# Step3 description:
# Install packages with "pip"
# cmd -> go to that 'dist folder' -> cd dist/
# cmd -> sudo python3 -m pip install util_functions-1.0.tar.gz
# voila!!! Now the util_functions module is now installed as part of site-packages
# now try importing that module

import util_functions

util_functions.print_todays_date()

# if we later decide to update the module's code, we have to repeat the above three steps to install
# any update to site-packages. If you do produce a new version of your module, be sure to assign a new version number
# in the setup.py file

# -----------------------------------------

# example:
from datetime import date


def print_todays_date():
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

# using multiple argument
# search for letters in a given phrase

def search4letters(phrase: str, letters: str):
    """Return a set of the 'letters' found in 'phrase'"""
    return sorted(set(phrase).intersection(set(letters)))


print(search4letters('Paranoid Android', 'aeiou'))


# -----------------------------------------

# assigning default value to positional argument

def search4letters_default_value(phrase: str, letters: str = 'aeiou'):
    """Return a set of the 'letters' found in 'phrase'"""
    return sorted(set(phrase).intersection(set(letters)))


print(search4letters_default_value('Paranoid Android'))
print(search4letters_default_value('Paranoid Android', 'dn'))

# -----------------------------------------

# keyword argument: if we refer the argument by their parameter name, then its called keyword argument
# for keyword argument, positional ordering  is no longer needed.

print(search4letters_default_value(letters='pr', phrase='Paranoid Android'))

# -----------------------------------------
