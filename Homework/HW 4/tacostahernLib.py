'''
Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will serve as the library for a variety of functions that need to be implemented.
First, there will be 2 functions that are used to convert from Radians to Degrees and from Degrees to Radians
respectively. The next two functions will be used to calculate retail prices from user input.

For HW 4, there will be functions for use in the first problem; first, a function to take in input from the
user, save it into a list, and then return that list. Second, a function used to sum up the total of that list
and apply a sales tax. Functions will also be made to get the subtotal price, final cost, and print out each item
'''

import math # for using pi value

#For HW 3
r2d = lambda radians: radians * (180 / math.pi) #lambda function. returns converted degrees value

d2r = lambda degrees: degrees * (math.pi / 180) #lambda function. returns converted radians value
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

calcRetailPrice = lambda cost, markUp: cost + (cost * markUp) #returns the retail price, called in getCost()

#For HW 4
def getItems(itemList): #Function to get input from user
    try: #Checking to see if they actually enter a number
        item = eval(input("Please enter an item price, or enter '0' to stop: ")) #Logic here is no price is 0
    except:
        print("ERROR: That is not a number!")
        return

    while item != 0:
        if item < 0: #Can't have negative prices either
            print("ERROR: A price cannot be negative.")
            item = eval(input("Please enter an item price, or enter '0' to stop: "))
        else:
            itemList.append(item)
            item = eval(input("Please enter an item price, or enter '0' to stop: "))

    return itemList #returns a (ideally) filled list

calculateTax = lambda itemList: sum(itemList) * .07 #Lambda function to return total tax

priceTotal = lambda itemList: sum(itemList) #Lambda function to return sum of itemList

finalTotal = lambda subtotal, tax: subtotal + tax #Lambda function which gets us the final price

def multiplyMatrix(a, b): #For solving the second problem

    productMatrix = list()
    if len(a) != 3 or len(b)!= 3: #Matrices need to be equal sizes of 9
        print("The matrices are not equal sizes!")
        return productMatrix

    for i in range(0,3):
        for j in range(0, 3):
            product = (a[i][0] * b[0][j]) + (a[i][1] * b[1][j]) + (a[i][2] * b[2][j])
            productMatrix.append(product)

    return productMatrix
        

