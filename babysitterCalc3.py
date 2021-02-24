

def main():

    print("\nBabysitting Calculator\n")
    print("Enter times using 24 hour format (e.g. 8pm is 20:00)")

    startTime = input("Starting time (hh:mm): ")
    endTime = input("Ending time (hh:mm): ")

    startHr, startMin = startTime.split(":")
    endHr, endMin = endTime.split(":")

    minWorked = ((int(endHr) * 60 + int(endMin)) - (int(startHr) * 60 + int(startMin)))
    
    if minWorked <= 0:
        print("Invalid Entry")

    elif int(endHr) < 21:
        pay = (2.5/60) * minWorked
        print("Total payment due: ${0:0.2f}".format(pay)) 
    elif int(startHr) >= 21:
        pay = (1.75/60) * minWorked
        print("Total payment due: ${0:0.2f}".format(pay))
    else:
        dayPay = (2.5/60) * ((21*60) - (int(startHr) * 60 + int(startMin)))
        eveningPay = (1.75/60) * ((int(endHr) * 60 + int(endMin)) - (21*60))
        totalPay = dayPay + eveningPay
        print("Total payment due: ${0:0.2f}".format(totalPay))

    print()
main()