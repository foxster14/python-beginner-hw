
from graphics import *

def main():

    win = GraphWin("Student Records",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("light grey")

    infile = open("Students.csv","r")
    infilename = "Students.csv"

    title = Text(Point(200,320), "File name: " + infilename)
    title.draw(win)

    count = len(infile.readlines())
    recordCount = Text(Point(200,250), "Record count: " + str(count))
    recordCount.draw(win)

    message = Text(Point(200,30),"Click on screen to continue")
    message.draw(win)

    win.getMouse()
    title.undraw()
    recordCount.undraw()
    infile.close()

    infile = open("Students.csv","r")
    outfile = open("Students_fixed.csv","w")

    # store the number of lines removed in a list
    count = [] 
    # Iterate through each line in file
    for line in infile.readlines():
        # Only write the lines to file that do not have Calamity or Newville in them
        if "Calamity" not in line and "Newville" not in line:
            outfile.write(line)
        # Use this to count how many lines are removed from the file
        else:
            count.append(line)

    # print how many lines were removed
    removed = Text(Point(200,250),"Records Removed: " + str(len(count)))
    removed.draw(win)

    # Print the new record count 
    win.getMouse()
    removed.undraw()
    infile.close()
    outfile.close()

    infile = open("Students_fixed.csv")
    infilename = "Students_fixed.csv"
    fileCount = len(infile.readlines())

    title = Text(Point(200,320), "File name: " + infilename)
    title.draw(win)
    recordCount = Text(Point(200,250),"Record Count: " + str(fileCount))
    recordCount.draw(win)

    print("end of program")

    win.getMouse()
    win.close()
main()