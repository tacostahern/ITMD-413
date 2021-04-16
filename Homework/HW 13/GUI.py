'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will use Python's tkinter GUI module and a class called
Coin to create a GUI that allows users to enter each coin they have in their possession,
and then compute and display the dollar and cents value of these coins. 
'''

from tkinter import *
from tkinter import ttk

class Coin():
    def __init__(self, quarter, dime, nickel, penny, half_dollar, dollar):
        self.__quarter = quarter
        self.__dime = dime
        self.__nickel = nickel
        self.__penny = penny
        self.__half_dollar = half_dollar
        self.__dollar = dollar

    def getQuarter(self):
        return self.__quarter

    def getDime(self):
        return self.__dime

    def getNickel(self):
        return self.__nickel
        
    def getPenny(self):
        return self.__penny

    def getHalfDollar(self):
        return self.__half_dollar

    def getDollar(self):
        return self.__dollar

    def setQuarter(self, quarter):
        self.__quarter = quarter

    def setDime(self, dime):
        self.__dime = dime

    def setNickel(self, nickel):
        self.__nickel = nickel

    def setPenny(self, penny):
        self.__penny = penny
    
    def setHalfDollar(self, half_dollar):
        self.__half_dollar = half_dollar

    def setDollar(self, dollar):
        self.__dollar = dollar

    def computeQuarters(self):
        return self.__quarter * .25

    def computeDimes(self):
        return self.__dime * .10

    def computeNickels(self):
        return self.__nickel * .05

    def computePennies(self):
        return self.__penny * .01

    def computeHalfDollars(self):
        return self.__half_dollar * .5

def calculate(quarters, dimes, nickels, pennies, half_dollars, dollars, window):
    coin = Coin(int(quarters.get()), int(dimes.get()), int(nickels.get()), int(pennies.get()), int(half_dollars.get()), int(dollars.get()))
    quartersValue = coin.computeQuarters()
    Label(window, justify = LEFT, text = quartersValue).grid(row = 1, column = 3, sticky = W)

    dimesValue = coin.computeDimes()
    Label(window, justify = LEFT, text = dimesValue).grid(row = 2, column = 3, sticky = W)
    
    nickelsValue = coin.computeNickels()
    Label(window, justify = LEFT, text = nickelsValue).grid(row = 3, column = 3, sticky = W)

    penniesValue = coin.computePennies()
    Label(window, justify = LEFT, text = penniesValue).grid(row = 4, column = 3, sticky = W)

    halfDollarsValue = coin.computeHalfDollars()
    Label(window, justify = LEFT, text = halfDollarsValue).grid(row = 5, column = 3, sticky = W)

    dollarsValue = coin.getDollar()
    Label(window, justify = LEFT, text = dollarsValue).grid(row = 6, column = 3, sticky = W)

    totalChangeValue = quartersValue + dimesValue + nickelsValue + penniesValue + halfDollarsValue + dollarsValue
    Label(window, justify = LEFT, text = totalChangeValue).grid(row = 7, column = 3, sticky = W)

def main():
    window = Tk()
    window.title("Change Counter")
    window.geometry("800x400")

    Label(window, justify = LEFT, text = "Enter the number of each coin type and click compute:", width = 20, wraplength = 150).grid(row = 0, column = 0, sticky = W)
    quarters = Label(window, text = "Quarters:").grid(row = 1, column = 0, sticky = E)
    quartersInput = Entry(window)
    quartersInput.grid(row = 1, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Quarter value: $").grid(row = 1, column = 2, sticky = E)

    dimes = Label(window, text = "Dimes:").grid(row = 2, column = 0, sticky = E)
    dimesInput = Entry(window)
    dimesInput.grid(row = 2, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Dime value: $").grid(row = 2, column = 2, sticky = E)

    nickels = Label(window, text = "Nickels:").grid(row = 3, column = 0, sticky = E)
    nickelsInput = Entry(window)
    nickelsInput.grid(row = 3, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Nickel value: $").grid(row = 3, column = 2, sticky = E)

    pennies = Label(window, text = "Pennies:").grid(row = 4, column = 0, sticky = E)
    penniesInput = Entry(window)
    penniesInput.grid(row = 4, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Penny value: $").grid(row = 4, column = 2, sticky = E)

    half_dollars = Label(window, text = "Half Dollars:").grid(row = 5, column = 0, sticky = E)
    halfDollarsInput = Entry(window)
    halfDollarsInput.grid(row = 5, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Half Dollar value: $").grid(row = 5, column = 2, sticky = E)

    dollars = Label(window, text = "Dollars:").grid(row = 6, column = 0, sticky = E)
    dollarsInput = Entry(window)
    dollarsInput.grid(row = 6, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Dollar value: $").grid(row = 6, column = 2, sticky = E)

    Label(window, justify = LEFT, text = "Total Change value: $").grid(row = 7, column = 2, sticky = E)
    totalChangeValue = Entry(window).grid(row = 7, column = 3, sticky = W)

    btn = ttk.Button(window, text = "Compute", command = lambda: calculate(quartersInput, dimesInput, nickelsInput, penniesInput, halfDollarsInput, dollarsInput, window))
    btn.grid(row = 7, column = 1)
    window.mainloop()

main()