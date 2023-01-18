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
print('bool value of empty string:', bool({1,2,3}))



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


