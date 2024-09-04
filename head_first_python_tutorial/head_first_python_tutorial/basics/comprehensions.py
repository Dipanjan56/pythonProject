"""Comprehensions: comprehensions are of 3 types:
1. list comprehension 2. dictionary comprehension 3. set comprehensions
but there is nothing like tuple comprehensions
"""

######################################################################################
from datetime import datetime
from pprint import pprint

""" list_comprehension {template}: [<expression val> <for val in list> <filters if any>]
list comprehension is faster and more optimized than the normal for loop
"""
# example:

# square all the list number from 1 to 10

# general syntax

squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(f'num list in general syntax: {squares}')

# list_comprehension syntax:

squares2 = [i ** 2 for i in range(1, 11)]
print(f'num list in list_comprehension: {squares}')

# ---------------------------

# print all substrings

s = 'abcde'
s_list = []
# general syntax
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        sub_string = s[i:j]
        s_list.append(sub_string)

print(f'substring with general syntax: {s_list}')

# ---------------------------
# print all substrings
# list comprehension

s_list2 = [s[i:j] for i in range(0, len(s)) for j in range(i + 1, len(s) + 1)]
print(f'substring with list comprehension: {s_list2}')

# ---------------------------

# print all substrings starts with a
s_list3 = [s[i:j] for i in range(0, len(s)) for j in range(i + 1, len(s) + 1) if s[i:j].startswith('a')]
print(f'substring starts with "a" with list comprehension: {s_list3}')

# --------------------------------

"""print all even numbers till 20"""

evens = [num for num in range(1, 21) if not num % 2]
print('even numbers: ', evens)

# --------------------------------

"""get the integer object from the below list as well also get the string object"""

data = [1, 'one', 2, 'two', 3, 'three']
nums = [i for i in data if isinstance(i, int)]
words = [i for i in data if isinstance(i, str)]

print(f'nums: {nums} | words: {words}')


######################################################################################

def convert_to_am_pm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


"""dictionary comprehensions{template}: 
[<expression of key,value> <for key, value in dictionary.items()> <filters if any>]"""

flight_dict = {'09:52': 'FREEPORT',
               '09:55': 'WESTEND',
               '11:45': 'ROCK SOUND',
               '12:00': 'TREASURE CAY',
               '17:00': 'FREEPORT',
               '18:45': 'WESTEND',
               '19:25': 'ROCK SOUND',
               '22:00': 'TREASURE CAY'}

"""task: 
1. convert flight times into am/pm
2. convert destinations from uppercase to title case
"""

flight_dict_2 = {}
for k, v in flight_dict.items():
    flight_dict_2[convert_to_am_pm(k)] = v.title()

pprint(flight_dict_2)
print()

"""now solve this using dictionary comprehension"""

flight_dict_new = {convert_to_am_pm(k): v.title() for k, v in flight_dict.items()}

pprint(flight_dict_new)
print()

"""just give the report for freeport in the above way"""

flight_dict_freeport = {convert_to_am_pm(k): v.title() for k, v in flight_dict.items() if v == 'FREEPORT'}

pprint(flight_dict_freeport)
print()

# ---------------------------------------

"""give the report of airport with times"""

"normal way"

report_dict = {}
for dest in set(flight_dict.values()):
    time_list = []
    for k, v in flight_dict.items():
        if v == dest:
            time_list.append(convert_to_am_pm(k))
    report_dict[dest.title()] = time_list

pprint(report_dict)
print()

# -------------------

"using comprehension"

report_dict = {dest.title(): [convert_to_am_pm(k) for k, v in flight_dict.items() if v == dest] for dest in
               set(flight_dict.values())}

pprint(report_dict)
print()

######################################################################################


"""set comprehensions{template}: {<expression val> <for val in set> <filters if any>}"""

"""find set of vowels in message"""

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel"

found = {letter for letter in vowels if letter in message}
print(found)

######################################################################################

"""generator {template}: (<expression val> <for val in list> <filters if any>)
dont be confused by thinking it as tuple comprehension as it doesn't exist.
It is much more like list comprehension and generates the same output
although its working mechanism is different than list comprehension 

listcomp produces all of its data prior to any other processing occuring, 
imagine your list comp is required to work with 10 million data, then
you have two big issues: 
1. you have to wait for the listcomp to process
those 10 million data items before doing anything else
2. you have to worry about RAM to hold 10 million data processing

But Generator produce data item one at a time, i.e, 
it releases data as soon as the data is produced by the generator's code. 
This means if you 10 million data items, the interpreter only needs to hold one data(at a time),
and any code that's waiting to consume the data items produced by the generator executes immediately,
that means, there is no waiting
"""

"""example: Process url"""

urls = ('http://google.com', 'http://oreilly.com', 'http://twitter.com')

"""USING LIST COMPREHENSION: 

you will experience a noticeable delay here, when the results appear, they are displayed in one go(all at once)
this is because the listcomp works through each of the URLs in urls tuple before making the results available for
the outer foor loop
"""

import requests

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

"""USING GENERATOR:

here you wont experience any delay as generator displayed result one by one, not in one go,
this is because generator process and sends data one at a time, as result as soon as it gets the resp
from URLs it sends the data to outer for loop immediately.
"""

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

"""EMBED GENERATOR INTO A FUNCTION:
for generator never use return statement as it cause the function to terminate
in our case we need something that returns the value but do not terminate the function 
as if function waits like suspended animation. For this use 'Yield' statement
"""


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, status, url, sep=' => ')

"""print as dictionary of url and res_len excluding status code"""

"""using dictionary comprehension"""
urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint(urls_res)

""" here undersocre '_' tells the code to ignore the https status code"""
######################################################################################
