# open a file and put some string into it:
# -------------------------
# Option 1: use open method with 'a' argument
from datetime import datetime
from pprint import pprint

todos = open('todos.txt', 'a')
# open method returns the file stream
# 'a' open the fie in append mode, now you can write the file using print method
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

todos.close()
# once done with your work, always close the file stream
# -------------------------
with open('todos.txt', 'a') as todos:
    print('New Comment', file=todos)

# --------------------------------------------------------------

# reading data from an existing file:

# -------------------------
# Option 1: 'reading' is open function's default method
file = open('todos.txt')
for line in file:
    print(line, end='')
file.close()
# end='' -> this wil suppress the print's newline-appending behavior, so extra new lines no longer appear om screen
# -------------------------

# -------------------------
# Option 2: use with statement
with open('todos.txt') as file:
    for line in file:
        print(line, end='')
# here we do not need the close method to close the file as with statement is smart enough to close the function
# automatically once done
# -------------------------

# -------------------------
# Option 3: use with statement and read function
with open('todos.txt') as file:
    contents = file.read()
    print(contents)
# here we file.read() will return all the contents of the file
# -------------------------

# --------------------------------------------------------------
# writing data from an existing file: use 'w' argument

file = open('todos.txt', 'w')
# this 'write' method will empty the file and then add the string
file.write('write something')
# this 'writelines' method will add new line to the file without clearing the data
file.writelines('\nwrite new line')
file.close()

# --------------------------------------------------------------
# open a new file for writing and fail if the file already exists: use 'r argument'
# file = open('todos_new.txt', 'x')
# file.write('write another new line')
# file.close()

# --------------------------------------------------------------

"""Reading CSV as a whole"""

with open('buzzers.csv') as raw_data:
    print(raw_data.read())

# --------------------------------------------------------------


"""Reading CSV as strings"""

with open('buzzers.csv') as raw_data:
    for line in raw_data.readlines():
        print(line)

# --------------------------------------------------------------

"""Reading CSV as lists"""

import csv

with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)

# --------------------------------------------------------------

"""Reading CSV as dictionaries"""

with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

# --------------------------------------------------------------


"""task: 
1. convert flight times into am/pm
2. convert destinations from uppercase to titlecase
"""


def convert_to_am_pm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as raw_data:
    """ignore the header info"""
    ignore = raw_data.readline()
    flights = {}
    for line in raw_data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint(flights)
print()

flights2 = {}

for k, v in flights.items():
    flights2[convert_to_am_pm(k)] = v.title()

pprint(flights2)

# ------------------

"""get the destination list using for loop"""

dest_list = []
for dest in flights2.values():
    dest_list.append(dest)
print(dest_list)

"""get the destination list of titlecase using for list comprehension"""

dest_list_comprehension = [dest.title() for dest in flights.values()]
print(dest_list_comprehension)

""" give the report of airport with times"""

" normal way"

report_dict = {}
for dest in set(flights.values()):
    time_list = []
    for k, v in flights.items():
        if v == dest:
            time_list.append(convert_to_am_pm(k))
    report_dict[dest.title()] = time_list

pprint(report_dict)
print()

# -------------------

"using comprehension"

report_dict = {dest.title(): [convert_to_am_pm(k) for k, v in flights.items() if v == dest] for dest in
               set(flights.values())}

pprint(report_dict)
print()
