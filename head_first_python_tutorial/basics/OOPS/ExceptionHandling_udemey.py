"""

Exception / Errors

Exceptions are simply disruptions to the flow of program


"""

"""
Python Exception Hierarchy

BASE EXCEPTION
   1. Exception
        a. Attribute Exception / Error
        b. Arithmetic Exception / Error
            1. ZeroDivision Error
            2. FloatingPoint Error
            3. Overflow Error
        c. EOF Exception (End of File)
        d. Name Exception
        e. and many more
   2. System Exit
   3. Generator Exit
   4. Keyboard Interrupt


"""





"""


Try and Except block


    try:
        {-----------}
    except:
        {---------}


"""


try:
    a = int(input("Enter the value for first number : "))
    b = int(input("Enter the value for second number : "))

    c = a / b

    print("Result is {}".format(c))

    print("ending")

except (ZeroDivisionError, ValueError):
    print("Please enter a valid number ")
else:
    print("Inside an Else block")
finally:
    print("I am always executed")
"""this else block will only be executed if there is no exception in the above try block, 
so if we want some operation to be executed after try block only everything works fine, then we use else block"""
print("This is outside Try Except block")

