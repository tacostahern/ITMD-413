'''
Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: The following program, SellItems, will solve two problems.
First, it will allow the user to enter any number of item prices and then
calculate the total for the items and apply a 7% sales tax. The item prices will
be stored in a Python list, with a loop being used to get the input and
calculate the total. The functions used will be created in the tacostahernLib
file created in HW 3.

Second, a function will be created that will be able to multiply two matrices
'''

from tacostahernLib import *
#Solving the first problem
itemList = list()
itemList = getItems(itemList)
tax = calculateTax(itemList)
subtotal = priceTotal(itemList)
finalCost = finalTotal(subtotal, tax)

print("Item Prices:",itemList)
print("Total price: $" + format(subtotal, ',.2f'))
print("Taxes: $" + format(tax, ',.2f'))
print("Final Cost: $" + format(finalCost, ',.2f'))

#Solving the second problem, where the function created is in tacostahernLib

#these input for testing purposes
#a = [[1,2,3],[4,5,6],[7,8,9]]
#b = [[0,2,4],[1,4.5,2.2],[1.1,4.3,5.2]]

#a = [[1,2,3],[4,5,6],[7,8,9]]
#b = [[1,2,3],[4,5,6],[7,8,9]]
#print(multiplyMatrix(a, b))

a = list()
b = list()

for i in range(0, 3): #For creating a list with 3 lists in it, like the rows in a matrix
    subList = list()
    for j in range(0, 3):
        num = eval(input("Please enter a value in the matrix: "))
        subList.append(num)
    a.append(subList)
        
for i in range(0, 3): #For creating a list with 3 lists in it, like the rows in a matrix
    subList = list()
    for j in range(0, 3):
        num = eval(input("Please enter a value in the other matrix: "))
        subList.append(num)
    b.append(subList)

print("Matrix A:", a)
print("Matrix B:", b)

print("Their product:", multiplyMatrix(a, b))


