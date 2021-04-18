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
        if quarter > 0:
            self.__quarter = quarter
        else:
            self.__quarter = 0

        if dime > 0:
            self.__dime = dime
        else:
            self.__dime = 0

        if nickel > 0:
            self.__nickel = nickel
        else:
            self.__nickel = 0

        if penny > 0:
            self.__penny = penny
        else:
            self.__penny = 0

        if half_dollar > 0:
            self.__half_dollar = half_dollar
        else:
            self.__half_dollar = 0

        if dollar > 0:
            self.__dollar = dollar
        else:
            self.__dollar = 0

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
        if quarter > 0:
            self.__quarter = quarter
        else:
            self.__quarter = 0

    def setDime(self, dime):
        if dime > 0:
            self.__dime = dime
        else:
            self.__dime = 0

    def setNickel(self, nickel):
        if nickel > 0:
            self.__nickel = nickel
        else:
            self.__nickel = 0

    def setPenny(self, penny):
        if penny > 0:
            self.__penny = penny
        else:
            self.__penny = 0

    def setHalfDollar(self, half_dollar):
        if half_dollar > 0:
            self.__half_dollar = half_dollar
        else:
            self.__half_dollar = 0

    def setDollar(self, dollar):
        if dollar > 0:
            self.__dollar = dollar
        else:
            self.__dollar = 0

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


def checkEntry(value): #For use in checking if the entry value is a number
    if value.get().isdigit():
        return int(value.get())
    else:
        print(value.get(), "is not a valid coin number!")
        return 0


def calculate(quarters, dimes, nickels, pennies, half_dollars, dollars, window): #calcylates and displays the actual coin values
    coin = Coin(checkEntry(quarters), checkEntry(dimes), checkEntry(
        nickels), checkEntry(pennies), checkEntry(half_dollars), checkEntry(dollars))
    quartersValue = coin.computeQuarters()
    quartersText = Label(window, justify=LEFT)
    quartersText.grid(row=1, column=3, sticky=W)
    quartersText.config(text="{:.2f}".format(quartersValue))

    dimesValue = coin.computeDimes()
    dimesText = Label(window, justify=LEFT)
    dimesText.grid(row=2, column=3, sticky=W)
    dimesText.config(text="{:.2f}".format(dimesValue))

    nickelsValue = coin.computeNickels()
    nickelsText = Label(window, justify=LEFT)
    nickelsText.grid(row=3, column=3, sticky=W)
    nickelsText.config(text="{:.2f}".format(nickelsValue))

    penniesValue = coin.computePennies()
    penniesText = Label(window, justify=LEFT)
    penniesText.grid(row=4, column=3, sticky=W)
    penniesText.config(text="{:.2f}".format(penniesValue))

    halfDollarsValue = coin.computeHalfDollars()
    halfDollarsText = Label(window, justify=LEFT)
    halfDollarsText.grid(row=5, column=3, sticky=W)
    halfDollarsText.config(text="{:.2f}".format(halfDollarsValue))

    dollarsValue = coin.getDollar()
    dollarsText = Label(window, justify=LEFT)
    dollarsText.grid(row=6, column=3, sticky=W)
    dollarsText.config(text="{:.2f}".format(dollarsValue))


    totalChangeValue = quartersValue + dimesValue + nickelsValue + \
        penniesValue + halfDollarsValue + dollarsValue
    totalChangeText = Label(window, justify=LEFT)
    totalChangeText.grid(row=7, column=3, sticky=W)
    totalChangeText.config(text="{:.2f}".format(totalChangeValue))



def main():
    window = Tk()
    window.title("Change Counter")
    window.geometry("800x400")

    Label(window, justify=LEFT, text="Enter the number of each coin type and click compute:",
          width=20, wraplength=150).grid(row=0, column=0, sticky=W)
    quarters = Label(window, text="Quarters:").grid(row=1, column=0, sticky=E)
    quartersInput = Entry(window)
    quartersInput.grid(row=1, column=1, sticky=W)
    Label(window, justify=LEFT, text="Quarter value: $").grid(
        row=1, column=2, sticky=E)

    dimes = Label(window, text="Dimes:").grid(row=2, column=0, sticky=E)
    dimesInput = Entry(window)
    dimesInput.grid(row=2, column=1, sticky=W)
    Label(window, justify=LEFT, text="Dime value: $").grid(
        row=2, column=2, sticky=E)

    nickels = Label(window, text="Nickels:").grid(row=3, column=0, sticky=E)
    nickelsInput = Entry(window)
    nickelsInput.grid(row=3, column=1, sticky=W)
    Label(window, justify=LEFT, text="Nickel value: $").grid(
        row=3, column=2, sticky=E)

    pennies = Label(window, text="Pennies:").grid(row=4, column=0, sticky=E)
    penniesInput = Entry(window)
    penniesInput.grid(row=4, column=1, sticky=W)
    Label(window, justify=LEFT, text="Penny value: $").grid(
        row=4, column=2, sticky=E)

    half_dollars = Label(window, text="Half Dollars:").grid(
        row=5, column=0, sticky=E)
    halfDollarsInput = Entry(window)
    halfDollarsInput.grid(row=5, column=1, sticky=W)
    Label(window, justify=LEFT, text="Half Dollar value: $").grid(
        row=5, column=2, sticky=E)

    dollars = Label(window, text="Dollars:").grid(row=6, column=0, sticky=E)
    dollarsInput = Entry(window)
    dollarsInput.grid(row=6, column=1, sticky=W)
    Label(window, justify=LEFT, text="Dollar value: $").grid(
        row=6, column=2, sticky=E)

    Label(window, justify=LEFT, text="Total Change value: $").grid(
        row=7, column=2, sticky=E)
    

    btn = ttk.Button(window, text="Compute", command=lambda: calculate(
        quartersInput, dimesInput, nickelsInput, penniesInput, halfDollarsInput, dollarsInput, window))
    btn.grid(row=7, column=1)
    window.mainloop()


main()
