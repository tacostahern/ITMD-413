'''
Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will serve as the library for a variety of functions that need to be implemented.
First, there will be 2 functions that are used to convert from Radians to Degrees and from Degrees to Radians
respectively. The next two functions will be used to calculate retail prices from user input.
'''

import math # for using pi value
def r2d(radians):
    return radians * (180 / math.pi)

def d2r(degrees):
    return degrees * (math.pi / 180)
print()
#Testing purposes
#print(r2d(1)) 
#print(d2r(360))

def getCost(markUp):
    wholesale = float(input("Enter the item's wholesale cost: "))

    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost:'))

    # Display the retail price.
    print('Retail price: $', format(calcRetailPrice(wholesale, markUp), ',.2f'))

def calcRetailPrice(cost, markUp): #returns the retail price, called in getCost()
    return cost + (cost * markUp)
    
    
    
