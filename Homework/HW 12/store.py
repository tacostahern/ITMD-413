'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
This program, store.py, will contain an abstract class called Store that 
will contain the attributes store name, address, availability, and sales
tax percentage. It will contain a constructor used to pass and set values,
getters and setters for the class attributes, a function is_store_open that
returns True if the store is open and False if the store is closed, and 2 
abstract methods: calculate_total_sales_tax, calculate_total_sales
'''

from abc import ABC, abstractmethod
class Store(ABC):

    def __init__(self, name, address, availability, sales_tax_percentage):
        self.__store_name = name
        self.__store_address = address
        self.__store_availability = availability
        self.__store_sales_tax_percentage = sales_tax_percentage

    def getName(self):
        return(self.__store_name)

    def getAddress(self):
        return(self.__store_address)
    
    def getAvailability(self):
        return(self.__store_availability)

    def getSalesTaxPercentage(self):
        return(self.__store_sales_tax_percentage)

    def setName(self, name):
        self.__store_name = name

    def setAddress(self, address):
        self.__store_address = address

    def setAvailability(self, availability):
        self.__store_availability = availability

    def setSalesTaxPercentage(self, sales_tax_percentage):
        self.__store_sales_tax_percentage = sales_tax_percentage

    def is_store_open(self):
        if self.__store_availability == "open":
            return True
        else:
            return False

    @abstractmethod
    def calculate_total_sales_tax(self):
        pass
    
    @abstractmethod
    def calculate_total_sales(self):
        pass