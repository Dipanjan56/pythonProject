# set: Set don't allow duplicate values
# empty set is initialised by set(), e.g.: s = set()
# set with values is being initialised by {object, object, .....}, e.g. s = {2, 4, 6, 7}

# In set, insertion order is not maintained for strings, so Unlike lists, which keep your objects arranged in the order
# in which you inserted them, set does not. Although you can sort them using sorted() function
# but for numbers, set maintain sorting order

# Being a set, this data-structure can perform set like operations, such as difference, intersection and union
# union: it works by combining sets, i.e. it will combine the objects of two sets

# difference: it tells you what values are not common /shared, but there is a trick:
# example1: set1 = {1, 2, 3, 4},  set2 = {1, 4, 5, 6, 3}, now if we do set1.difference(set2), then it will show the
# numbers which exist in set1 but not in set2, hence output will be: {2}
# example2: set1 = {1, 2, 3, 4},  set2 = {1, 4, 5, 6, 3}, now if we do set2.difference(set2), then it will show the
# numbers which exist in set2 but not in set1, hence output will be: {5, 6}

# intersection: it reports on commonality, i.e. it will give the common objects shared between two sets


# -----------------------------------------

# initialise empty set
s1 = set()
print(f'empty set: {s1}')

# initialise set with values
s2 = {1, 2, 3, 2, 5, 2, 4, 4, 7}
print(f'set with values: {s2}')

# initialise set using shorthand for string objects
s3 = set('abcdef')
print(f'set using shorthand: {s3}')

# -----------------------------------------

# 1. Add values in set
my_set = {1, 2, 3}
print('before adding value: ', my_set)
my_set.add(4)
my_set.add(2)

print('after adding value: ', my_set)

# -----------------------------------------

# 2. Remove values from set
my_set = {1, 2, 3}
print('before removing value: ', my_set)
my_set.remove(1)

print('after removing value: ', my_set)

# -----------------------------------------

# 3. Discard(element): Removes the specified element from the set, but does not raise an error if the element is not present.

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

my_set.discard(5)

# -----------------------------------------

# 4. pop(): Removes and returns a random element from the set. Raises a KeyError if the set is empty.
my_set = {1, 2, 3}
popped_element = my_set.pop()
print(popped_element)  # Output: Random element from the set
print(my_set)          # Output: Remaining elements

# -----------------------------------------

# 5. clear(): Removes all elements from the set, making it an empty set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# -----------------------------------------

# 6. update(iterable): Adds multiple elements to the set (can pass a list, tuple, or another set).

my_set = {1, 2}
my_set.update([3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# -----------------------------------------

# 7.  issubset(set): Returns True if the set is a superset of another set (i.e., it contains all elements of the other set).

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True

# -----------------------------------------

# 8. copy(): Returns a shallow copy of the set.
set1 = {1, 2, 3}
set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3}

# -----------------------------------------


# Convert list to set
num_list = [9, 6, 1, 2, 3, 2, 5, 2, 4, 4, 7]
num_set = set(num_list)
print(f'Convert list to set: {num_set}')

# -----------------------------------------

# Sorting of set for string objects
unsorted_str_list = ['e', 'a', 'd', 'n', 'g', 'c', 'b']
print(f'unsorted list: {unsorted_str_list}')
unsorted_str_set = set(unsorted_str_list)
print(f'unsorted set: {unsorted_str_set}')
sorted_str_set = sorted(unsorted_str_list)
print(f'sorted set: {sorted_str_set}')

# -----------------------------------------

# union [numbers]
num_set1 = {1, 2, 3, 4}
num_set2 = {4, 5, 6}
union_num_set = num_set1.union(num_set2)
print(f'union num_set: {union_num_set}')

# union [string]
str_set1 = {'e', 'a', 'd', 'g', 'c', 'b'}
str_set2 = {'h', 'f', 'g'}
unsorted_union_str_set = str_set1.union(str_set2)
print(f'unsorted_union_str_set: {unsorted_union_str_set}')
sorted_union_str_set = sorted(unsorted_union_str_set)
print(f'sorted_union_str_set: {sorted_union_str_set}')

# -----------------------------------------

# difference [numbers]
num_set1 = {1, 2, 3, 4}
num_set2 = {1, 4, 5, 6, 3}
diff_num_set1 = num_set1.difference(num_set2)
print(f'diff_num_set1: {diff_num_set1}')
diff_num_set2 = num_set2.difference(num_set1)
print(f'diff_num_set2: {diff_num_set2}')

# -----------------------------------------

# intersection
num_set1 = {1, 2, 3, 4}
num_set2 = {1, 4, 5, 6, 3}
intersection_num_set1 = num_set1.intersection(num_set2)
print(f'intersection_num_set1: {intersection_num_set1}')
intersection_num_set2 = num_set2.intersection(num_set1)
print(f'intersection_num_set2: {intersection_num_set2}')

# example: identify vowels in string
word = 'hello'
vowels = set('aeiou')
found = vowels.intersection(set(word))
print(f'vowels found in the word: {found}')

# -----------------------------------------


" iterating through set"

num_set = {1, 4, 5, 6, 3}

# approach 1:
for num in num_set:
    print(num)

# approach 2:
for i in range(len(list(num_set))):
    print(f'index: {i} | value: {list(num_set)[i]}')

#approach 3:
for index, element in enumerate(list(num_set)):
    print(f'index: {index} | value: {element}')


