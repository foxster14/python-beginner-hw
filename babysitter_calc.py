
def main():

    # Print introduction
    print("\nBabysitting Calculator\n")
    print("Enter the times using a 24 hour format (e.g. 8pm is 20:00)")

    startHr, startMin = input("Starting Time (hh:mm): ").split(":")
    endHr, endMin = input("Ending time (hh:mm): ").split(":")

    startHrInt = int(startHr)
    startMinInt = int(startMin)
    endHrInt = int(endHr)
    endMinInt = int(endMin)

    #minutesWorked = (endHrInt*60 + endMinInt) - (startHrInt*60 - startMinInt)
    startHrConvert = startHrInt * 60
    endHrConvert = endHrInt * 60

    if startHrInt >= 21:
        eveningPay = ((endHrConvert + endMinInt) - (startHrConvert + startMinInt)) * (1.75/60)
        print("Total payment due: ${0:0.2f}".format(eveningPay))

    elif endHrInt < 21:
        dayPay = ((endHrConvert + endMinInt) - (startHrConvert + startMinInt)) * (2.5/60)
        print("Total payment due: ${0:0.2f}".format(dayPay))
    
    else:
        dayPay = (2.5/60) * ((21 * 60) - (startHrConvert + startMinInt))
        eveningPay = (1.75/60) * ((endHrConvert + endMinInt) - (21*60))
        totalPay = eveningPay + dayPay
        print("Total payment due: ${0:0.2f}".format(totalPay))

main()