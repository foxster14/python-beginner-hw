import re

def main():
    # Print title
    print("\n   Names Database\n")

    numberOfNames = eval(input("How many names you want to store? "))
    print()

    # Print directions
    print("Please Enter the names starting with")
    print("upper case letter, followed by lower case letters\n")

    outfile = open("name_database.txt","w")
    
    for i in range(numberOfNames):
        names = input("Name " + str(i+1) + " >> Enter the name: ").capitalize()
        outfile.write(names)
    print()
    print("Names stored on to the File.")
    print()
    outfile.close()

    search = input("Do you want to search any name? (Y/N) : ").upper()

    if search == "N":
        print("Thank You!")
    
    elif search == "Y":
        letter = input("Enter the 1st letter of the name (upper-case): ").upper()
        infile = open("name_database.txt","r")
        
        readfile = infile.read()
        namesList = re.findall('([A-Z][a-z]+)', readfile)

        for i in namesList:
            if i[0] == letter:
                print(i) # This only works because it is inside of the for loop
        if letter not in namesList:
            print("No names found!")
        
    outfile.close()
main()