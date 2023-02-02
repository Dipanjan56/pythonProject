# tuple: tuple is just like a list, but immutable, so once you initialise it, you can not change a tuple
# tuple is initialised by PARENTHESES: () or tuple()
# tuple with values is initialised like this: num_tuple = (1,2,4,5,7)

# for creating a tuple, there should be a comma, as single object tuple without comma returns the object type

# -----------------------------------------

# initialise empty tuple
t1 = ()
print(f'empty tuple: {t1}')

t2 = tuple()
print(f'empty tuple: {t2}')

# initialise tuple with values
t3 = (1, 2, 3, 2, 5, 2, 4, 4, 7)
print(f'tuple with values: {t3}')

# initialise set using shorthand for string objects
t4 = tuple('abcdef')
print(f'tuple using shorthand: {t4}')

# initialise single object tuple[without comma]: it will not create a tuple, it will create the object we store

single_str_tuple = ('a')
print(f'single_str_tuple: {single_str_tuple} | type: {type(single_str_tuple)}')

single_num_tuple = (1)
print(f'single_num_tuple: {single_num_tuple} | type: {type(single_num_tuple)}')

# initialise single object tuple[with comma]: it will not create a tuple, it will create the object we store

single_str_tuple = ('a',)
print(f'single_str_tuple: {single_str_tuple} | type: {type(single_str_tuple)}')

single_num_tuple = (1,)
print(f'single_num_tuple: {single_num_tuple} | type: {type(single_num_tuple)}')

# -----------------------------------------
