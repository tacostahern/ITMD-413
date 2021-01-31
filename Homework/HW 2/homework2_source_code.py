'''
Author: Tony Acosta Hernandez
Class: ITMD 413
Date: 01/30/21
Program Description: This program will do 2 things. It will take the current
populations of USA and Mexico, as well as the decresing population rate and
increasing population rate of both, respectively. It will then display the
populations of both countries every year until the population of Mexico exceeds
that of the USA.

The program will then simulate a Troubleshooting chart for a Diesel Engine
'''

#Start of first problem
usaPop = 328200000
usaPopRate = 0.53

mexicoPop = 127600000
mexicoPopRate = 1.06
counter = 0;

while usaPop > mexicoPop:
    usaPop = usaPop - (usaPop * .0053)
    mexicoPop = mexicoPop + (mexicoPop * .0106)
    counter += 1
    print("Year ", counter)
    print("USA Population: ", format(usaPop, '.0f'))
    print("Mexico Population: ", format(mexicoPop, '.0f'))

print("Number of years it took for Mexico's population to overtake USA:", counter, "years")

# Start of second problem
lightStatus = input("What color are the status lights? Enter Green, Red, or Amber: ")

if lightStatus == "Green":
    print("Do restart procedure")
elif lightStatus == "Red":
    print("Shut off all input lines and check meter #3")
    meter3 = eval(input("What is the value in meter #3? "))

    if meter3 >= 50:
        print("Measure flow velocity at inlet 2B")
        flowVelocity = input("What is the flow velocity? Enter High, Normal, or Low: ")

        if flowVelocity == "High" or flowVelocity == "Low":
            print("Refer unit for factory service")
        elif flowVelocity == "Normal":
            print("Refer to inlet service manual")
        else:
            print("That is not a valid flow velocity!")
    else:
        print("Check main line for test pressure")
        testPressure = input("What is the test pressure? Enter High, Normal, or Low: ")

        if testPressure == "High" or testPressure == "Low":
            print("Refer to main line manual")
        elif testPressure == "Normal":
            print("Refer to motor service manual")
        else:
            print("That is not a valid test pressure!")

elif lightStatus == "Amber":
    print("Check fuel line service routine")
else:
    print("That is not a valid light status color!")


