 ###############################
 # Understanding how a counter/index variables works inside a for loop
 ###############################
 
valuesList = ["10","20","5"]

counter = 0
for num in valuesList:
    counter = counter + 1
    print(counter,"here")


counter = 0
for num in valuesList:
    counter = str(counter) + num
    print(counter,"here")


counter = 0
for num in valuesList:
    counter = counter + eval(num)
    print(counter,"here")


    #counter = counter + eval(num)
# Adds up the integer version of each number with each iteration
    # Stores the sum of values in a variable so they can be used in the if statement
