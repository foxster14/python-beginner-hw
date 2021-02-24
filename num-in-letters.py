#####################################
# Filename: num-in-letters.py
# Author: Sarah Fox
# Date: 01/04/2019
# A program that gets number from user and prints it out in letters 
#####################################
'''
START
    Create comment header
    Get input from user between 1 and 10
    Create a list of numbers (spelt out in letter form)
    If the number is less than or equal to 10 and greater than or equal to 0
        Print the number spelt out in letters using the list to index from
    If the number is greater than 10 or less than 0
        Print invalid option 
END
'''

def main():

    print("=" * 30)
    # Get input from user
    number = eval(input("Enter a number from 0 to 10: "))

    # List the numbers in letters to index from
    numberLetters = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

    if number <= 10 and number >= 0:
        print("Number", number,"in Letters:",numberLetters[number])
        print("=" * 30)
    else:
        print("Invalid entry")
main()