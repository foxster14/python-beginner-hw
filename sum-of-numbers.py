'''
START
    Create comment header
    Get input from user for x number of variables
    Split the input into a list so it can be iterated 
    Create a variable equal to 0 to index through the for loop
    Create a for loop for every number in the list of variables
        Convert the numbers from strings to integers so they can be added together
        Add each integer value to itself and store inside of the index variable
    If the sum of the values if less than 100
        Print the sum and state it is less than 100
    If the sum of the values is greater than 100
        Print the sum and state it is greater than 100
    If the sum is equal to 100
        Print the sum and state it is equal to 100
END
'''

def main():
    print()

    # Get input from user for x number of values
    # Convert string of values into a list by splitting on the comma
    valuesList = input("Enter the list of Values: ").split(",")
    
    # Create a variable that can be used to index through the loop
    counter = 0
    for num in valuesList:
        # Adds up the integer version of each number with each iteration
        # Stores the sum of values in a variable so they can be used in the if statement
        #counter = str(counter) + num
        counter = counter + eval(num)
    
    # If the sum of values is less than 100, print that its less than 100
    if counter < 100:
        print("Sum of numbers you entered:", counter,"is Lesser than 100")

    # If the sum of values if greater than 100, print that it is greater than 100
    elif counter > 100:
        print("Sum of numbers you entered:", counter, "is Greather than 100")

    # The only possibility left is that sum is equal to 100 because is a
    # The program will throw an error right away if the inputs are not numbers
    else:
        print("Sum of numbers you entered:", counter, "is Equal to 100")
    
    print()    
main()