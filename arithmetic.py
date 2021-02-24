####################################
# Filename: arithmetic.py
# Author: Sarah Fox
# Date: 01/04/2020
####################################
'''
START
END
'''

def main():
    # Print introduction
    print("ARITHMETIC OPERATIONS")

    # Get input from user for two values
    value1, value2 = eval(input("Enter the 2 values: "))
    print()

    # print menu 
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print()

    # Get input from user for menu selection
    option = eval(input("Enter your option number: "))

    if option == 1:
        print("Addition:", value1 + value2)
    
    elif option == 2:
        print("Subtraction:", value1 - value2)
    
    elif option == 3:
        print("Multiplication:", value1 * value2)

    elif option == 4:
        print("Division:", value1 / value2)
    
    else:
        print("Invalid option!")




main()