# list: an ordered mutable collection of objects -> it is dynamic, mutable and heterogeneous in nature
# dynamic -> it can grow and hrink in runtime
# mutable -> you can change a list at anytime by adding, removing or changing objects
# heterogeneous -> you do not need to predeclare the type of the object you are storing and also you can mix'n'match different tyoe of objects in one list
# The object it stores are ordered sequentially in slots
# duplicate values can be stored in a single list
# list always enclosed with SQUARE BRACKETS
# Python lets you access the list relative to each end,
# i,e. positive index count start from left to right (0,1,2,...,end_index) -> for this, start_index = 0
# and negative index count starts from right to left (-end_index,...., -3, -2, -1) -> for this, start_index = -1
# so it is very easy to get first and last value of the list -> num_list[0] = first value, num_list[-1] = last value

# examples ->
num_list = [0, 1, 2, 3, 4, 5]
# get the length of the list
print(f'size of the list: {len(num_list)}')

# check if a number is present in list ->
if 4 in num_list:
    print('4 is present in the list')
# check if a number is absent in list ->
if 6 not in num_list:
    print('6 is not present in the list')

# -------------------------------------------------------------------

# list has 5 useful methods:
# append(object value), remove(object value), pop(index value), extend(list), insert(index value, object value)

# append(object value): adds any object at the end of the list
num_list.append(6)
print(f'list after appending value: {num_list}')
num_list.append(7)
# adding duplicate value
num_list.append(6)
print(f'list after appending duplicate value: {num_list}')

# -------------------------------------------------------------------

# remove(object value): removes the first occurrence of the object value
num_list.remove(6)
print(f'list after removing value: {num_list}')

# -------------------------------------------------------------------

# pop(index value[optional]): removes and returns an object from an existing list on the object's index value
num = num_list.pop(2)
print(f'list after popping from 2nd position: {num_list}')
print(f'popped value: {num}')
# if we dont give any index value, then by default it removes the last element of the list
num = num_list.pop()
print(f'list after popping from default position: {num_list}')
print(f'popped value: {num}')

# -------------------------------------------------------------------

# extend(list): takes a second list and adds each  of its objects to an existing list.
# This method is very useful for combining two list
new_list = [8, 9, 10]
num_list.extend(new_list)
print(f'list after extending another list: {num_list}')

# -------------------------------------------------------------------

# insert(index value, object value): insert an object before the specified index value into an existing list
num_list2 = [2, 3, 4]
print(f'list before inserting the object: {num_list2}')
# inserting at first position
num_list2.insert(0, 1)
print(f'list after inserting the object: {num_list2}')
# inserting at any middle position
num_list2.insert(2, 'two-and-a-half')
print(f'list after inserting the object: {num_list2}')
# but it is not possible to insert a value at the end of the list, for that we need to use append method

# -------------------------------------------------------------------

# Convert a string into list
phrase = "Don't panic!"
plist = list(phrase)
print(f'original string: {phrase}')
print(f'converted list from string: {plist}')

# convert "Don't panic" to "on tap" by using list methods
plist = plist[1:8]
plist.remove("'")
# Swapping last two elements of a list
plist.extend([plist.pop(), plist.pop()])
# removing space from 3rd position and inserting it on 2nd position
plist.insert(2, plist.pop(3))

# Convert list into string
new_phrase = ''.join(plist)
print(f'converted string from list: {new_phrase}')

# -------------------------------------------------------------------

# Swap last two elements of a list
new_list = [1, 2, 3, 4]
print(f'original list: {new_list}')
new_list.extend([new_list.pop(), new_list.pop()])
print(f'list after swapping last two values: {new_list}')

# -------------------------------------------------------------------

# copying a list can be done by two ways:
# 1. SHALLOW COPY: copying he reference of the first list, but in this case of you change any object value of any of the
# list, then both the list will be changed
l1 = [1, 2, 3, 4]
l2 = l1

print(f'after copying, first list: {l1} | second list {l2}')
l2.append(5)
print(f'SHALLOW COPY => after changing second list, first list: {l1} | second list {l2}')

# 2. DEEP COPY: copying the object values from one list to another, but in this case of you change any object value
# of any of the list, then another list will not get changed
l1 = [1, 2, 3, 4]
l2 = l1.copy()

print(f'after copying, first list: {l1} | second list {l2}')
l2.append(5)
print(f'DEEP COPY => after changing second list, first list: {l1} | second list {l2}')

# -------------------------------------------------------------------

# List Slicing
# We can use start, stop and step inside a list -> list[start(inclusive):stop(exclusive):step]
# default value of start is 0
# default value of stop is the maximum value allowable for the list
# default value of step is 1

word = 'abcdefghijk'
letters = list(word)
print(f'original letter: {letters}')

# print Every third letter(but not including) index location 10
output = letters[0:10:3]
print(f'print Every third letter(but not including) index location 10: {output}')

# Print the word skipping first 3 letters
output = letters[3:]
print(f'Print the word skipping first 3 letters: {output}')

# print all letters upto(but not including) index value 10
output = letters[:10]
print(f'print all letters upto(but not including) index value 10: {output}')

# print the first 10 letters
output = letters[:9]
print(f'print the first 10 letters: {output}')

# print the last 5 letters
output = letters[-5:]
print(f'print the last 5 letters: {output}')

# reverse the list
output = letters[::-1]
# here start and stop are defaulted, i.e. start_index = 0, stop_index = max value
print(f'reverse the list: {output}')
# converting list into string
output_string = ''.join(output)

# print every third letter including first one
output = letters[::2]
print(f'print every third letter including first one: {output}')

# Covert "Don't Panic!" to "on tap" using slicing
s = "Don't panic"
print(f'original string: {s}')
l = list(s)
new_s = ''.join(l[1:3]) + ''.join([l[5], l[4], l[7], l[6]])
print(f'converted string: {new_s}')

# NOTE: If you want to change the original list in runtime, then use all the 5 list methods
# but if you want the original list not get impacted/altered in runtime, then use list slicing.


# -------------------------------------------------------------------

# list : for loop

num_list = [1, 2, 3, 4, 5]

for num in num_list:
    print(num)

s = 'abcde'
s_list = list(s)

for char in s_list:
    print(char)
