###############################
# Filename: studentRecords.py
# Author: Sarah Fox
# A program that appends data to a file and displays the file count in a graphics window
###############################

from graphics import*

def main():

    # Create graphics window
    win = GraphWin("Student Records",400,400)
    win.setBackground("light grey")
    win.setCoords(0,0,400,400)

    # Open file and store filename
    infile = open("Students.csv","r")
    infileName = "Students.csv"

    # Print file name to the graphics window
    title = Text(Point(200,320), "File name: " + infileName )
    title.draw(win)

    # Count how many lines are in the file
    count = len(infile.readlines())

    # Print the number of lines to graphics window
    recordCount = Text(Point(200,250), "Record Count: " + str(count))
    recordCount.draw(win)

    # Prompt user to click to continue 
    message = Text(Point(200,30),"Click on screen to continue")
    message.draw(win)

    # Erase everything from the graphics window once the user clicks
    win.getMouse()
    recordCount.undraw()
    title.undraw()
    message.undraw()

    # Need to close and re-open the file so that it can be appended
    infile.close()
    outfile = open("Students.csv","a")
    
    # Open the append file so we can read the data and count the # of lines
    infile = open("Append.csv","r")
    count = len(infile.readlines())

    # Print how many records are in the append file 
    title = Text(Point(200,280),"Records appended: " + str(count))
    title.draw(win)

    # Prompt user to click to continue
    message = Text(Point(200,30),"Click on screen to continue")
    message.draw(win)

    # Clear graphics window when user clicks
    win.getMouse()
    message.undraw()
    title.undraw()

    # Need to close and reopen file so we can read from it again
    infile.close()
    infile = open("Append.csv","r")

    # Append the lines from Append.csv to the end of the Students.csv file
    # Since the file was opened for appending, I can use the outfile.write()
    # and not have to worry that the file will get overwritten
    # I made sure that the Students.csv file already had a newline character at the bottom so the appended data would get placed in there correctly
    for line in infile.readlines():
        outfile.write(line)
    
    # Need to close the outfile for the changes to take place
    outfile.close()
    infile.close()
    # Need to reopen the original file to count the records
    infile = open("Students.csv","r")

    # Count how lines are in the file 
    fileCount = len(infile.readlines())

    # Print file name and record count to graphics window
    title = Text(Point(200,320), "File name: " + infileName)
    title.draw(win)
    recordCount = Text(Point(200,250), "Record count: " + str(fileCount))
    recordCount.draw(win)

    message = Text(Point(200,30),"Click on screen to close")
    message.draw(win)

    print("end of program")

    win.getMouse()
    win.close()

main()