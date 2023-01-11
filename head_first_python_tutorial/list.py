# list: an ordered mutable collection of objects -> it is dynamic, mutable and heterogeneous in nature
# dynamic -> it can grow and hrink in runtime
# mutable -> you can change a list at anytime by adding, removing or changing objects
# heterogeneous -> you do not need to predeclare the type of the object you are storing and also you can mix'n'match different tyoe of objects in one list
# The object it stores are ordered sequentially in slots
# duplicate values can be stored in a single list
# list always enclosed with SQUARE BRACKETS

# example ->
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
