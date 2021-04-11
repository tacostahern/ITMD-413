'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will contain a class called Restaurant, a child of 
the Store class. On top of the attributes from store, this class will also have the
attributes of total number of people served, max occupancy, current occupancy, price
per person. There will be a constructor for passing and setting values, as well as 
methods seat_patrons, serve_patrons, checkout_patrons, and getters and setters. Additionally,
the abstract methods calculate_total_sales_tax and calculate_total_sales will be implemented
in this program
'''

from store import *
class Restaurant(Store):

    def __init__(self, name, address, availability, sales_tax_percentage, people_served, max_occupancy, current_occupancy, price_per_person):
        self.__people_served = people_served
        self.__max_occupancy = max_occupancy
        self.__current_occupancy = current_occupancy
        self.__price_per_person = price_per_person
        Store.__init__(self, name, address, availability, sales_tax_percentage)

    def getPeopleServed(self):
        return(self.__people_served)

    def getMaxOccupancy(self):
        return(self.__max_occupancy)

    def getCurrentOccupancy(self):
        return(self.__current_occupancy)

    def getPricePerPerson(self):
        return(self.__price_per_person)

    def setPeopleServed(self, people_served):
        self.__people_served = people_served

    def setMaxOccupancy(self, max_occupancy):
        self.__max_occupancy = max_occupancy

    def setCurrentOccupancy(self, current_occupancy):
        self.__current_occupancy = current_occupancy

    def setPricePerPerson(self, price_per_person):
        self.__price_per_person = price_per_person

    def seat_patrons(self, people_to_sit):
        if (people_to_sit + getCurrentOccupancy()) > getMaxOccupancy():
            print("We are at a capacity, we appreciate your patience")
            return False
        else:
            setCurrentOccupancy(people_to_sit + getCurrentOccupancy())
            print("Welcome to", Store.getName())
            return True

    def serve_patrons(self, people_to_serve):
        setPeopleServed(people_to_serve + getPeopleServed())
        return "People Served:", getPeopleServed()

    def checkout_patrons(self, people_to_checkout):
        setCurrentOccupancy(getCurrentOccupancy() - people_to_checkout)
        return "Current Occupancy:", getCurrentOccupancy()

    def calculate_total_sales_tax(self):
        return((Restaurant.getPricePerPerson(self) * Restaurant.getPeopleServed(self)) * Store.getSalesTaxPercentage(self))
    
    def calculate_total_sales(self):
        return ((Restaurant.getPricePerPerson(self) * Restaurant.getPeopleServed(self)) + Restaurant.calculate_total_sales_tax(self))
    
