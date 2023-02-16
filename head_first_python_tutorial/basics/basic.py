# We think - Python support both call-by-value and call-by-reference for function arguments
# [see example in page 184 -187 (Head First Python)]

# In python variables are not like the variables like other programming languages,
# here variable means object reference, i.e. it is useful to think of the value stored in the variable as being the
# memory address of the value, not its actual value. Its the memory address that passed into the function,
# not the actual value
# Hence, Python's function support what's ,ore correctly called call-by-reference call semantics

# if the argument value is mutable, then call-by-reference apply
# if the argument value is immutable, then call-by-value apply


# importing a module in current project
import functions_and_modules

print(functions_and_modules.convert_number_to_string(1))

# -----------------------------------------

# input from console/ user input

word = input('Provide a word: ')
print(word)

# -----------------------------------------

# bool value of 0, None, empty string or any empty data structure returns False

print('bool value of 0:', bool(0))
print('bool value of None:', bool(None))
print('bool value of empty string:', bool(''))
print('bool value of empty data structure:', bool({}))

# bool value of any number except 0, non-empty string pr any data-structure with values  returns True


print('bool value of 1:', bool(1))
print('bool value of -1:', bool(-1))
print('bool value of None:', bool('asd'))
print('bool value of empty string:', bool({1, 2, 3}))

# -----------------------------------------

# if else

y = 5

if y > 6:
    x = 10
else:
    x = 20

print(f'if else: x = {x}, y = {y}')

# -----------------------------------------

# if else using ternary operator

x = 10 if y > 6 else 20

print(f'if else using ternary operator: x = {x}, y = {y}')
