'''
Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This will be the main program that will utilize the functions saved in
tacostahernLib. It will convert values from the user from radians to degrees and degrees to
radians.
'''

from tacostahernLib import *

radians = eval(input("Please enter a radians value to convert to degrees: "))
print("The value of", radians, "radians in degrees is", r2d(radians))

degrees = eval(input("Please enter a degrees value to convert to radians: "))
print("The value of", degrees, "degrees in radians is", d2r(degrees))

markUp = 2.5 #Markup percentage
repeat = 'y'

#process on or more items
while repeat == 'y' or repeat == 'Y': #checking for both cases
    #use our method to get wholesale cost
    getCost(markUp) #pass markUp variable into it so we can calculate the retail price

    repeat = input("Do you have another item? (Enter 'y' for yes): ")
