try:
    with open('myfile.txt') as file:
        file_data = file.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('This operation is anot allowed')
except:
    print('Some other error occured')

#################################################################

"""Now use a generalised error message for all the errors using catch-exception."""

try:
    with open('myfile.txt') as file:
        file_data = file.read()
    print(file_data)
except Exception as err:
    print('Some error occured', str(err), sep=': ')

#################################################################

"""raise runtime error if output is wrong"""


def get_num(num: int):
    if num > 15:
        print(f'num: {num} is in the expected range')
    else:
        raise Exception(f'num: {num} is not in the expected range')


try:
    get_num(10)
finally:
    print('end of operation')

#################################################################
