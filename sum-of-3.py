def main():

    numInput = input("Enter the list of values: ")
    numList = numInput.split(",")
    
    count = 0
    for i in numList:
        count = count + eval(i)
    
    if count > 100:
        print("Sum of numbers you entered:", count, "is Greater than 100")
    elif count < 100:
        print("Sum of numbers you entered:", count, "is Lesser than 100")
    else:
        print("Sum of numbers you entered:", count, "is Equal to 100")
    
main()