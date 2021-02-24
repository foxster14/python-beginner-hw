
def main():

    # Print introduction
    print("\nProgram to find the divisibility of a number\n")

    # Get input from user
    divisor = eval(input("You need to find the divisibility of? "))
    number = eval(input("Enter a number: "))

    print()
    if number % divisor == 0:
        print("The number", number, "is divisible by", divisor, ".")
    else:
        print("The number", number, "is not divisible by", divisor, ".")


main()