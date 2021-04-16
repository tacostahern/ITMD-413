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
        return self.__dime * .1

    def computeNickels(self):
        return self.__nickel * .05

    def computePennies(self):
        return self.__penny * .01

    def computeHalfDollars(self):
        return self.__half_dollar * .5

def main():
    window = Tk()
    window.title("Change Counter")
    window.geometry("800x400")

    Label(window, justify = LEFT, text = "Enter the number of each coin type and click compute:", width = 20, wraplength = 150).grid(row = 0, column = 0, sticky = W)
    quarters = Label(window, text = "Quarters:").grid(row = 1, column = 0, sticky = E)
    quartersInput = Entry(window).grid(row = 1, column = 1, sticky = W)
    Label(window, justify = LEFT, text = "Quarter value: $").grid(row = 1, column = 2)
    quartersValue = Entry(window).grid(row = 1, column = 3, sticky = W)

    window.mainloop()

main()