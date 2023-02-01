# open a file and put some string into it:
# -------------------------
# Option 1: use open method with 'a' argument

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
