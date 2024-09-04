# iterate over this list
num_list = [1, 2, 3, 4, 5]
for num in num_list:
    print(num)

# print first 5 numbers -> it will print -> 0, 1, 2, 3, 4
for num in range(5):
    print(num)

# print first 5 number starting from 1
for num in range(1, 6, 1):  # range can be written as range(start(inclusive), end(exclusive), increment/decrement)
    print(num)

# print even values till 10
print(list(range(0, 10, 2)))

# print all characters from the string
word = "abcdef"
for letter in word:
    print(letter)

my_set = {1, 2, 3, 4, 5}

# # using switch case
# for element in my_set:
#     match element:
#         case 1:
#             print("Found 1!")
#         case 2:
#             print("Found 2!")
#         case 3:
#             print("Found 3!")
#         case _:
#             print("Found an element not matching the specific cases.")
