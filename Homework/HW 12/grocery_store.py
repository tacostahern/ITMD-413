'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will contain a class called GroceryStore, a child of
the Store class. On top of the attributes of store, it will contain additional attributes
Total revenue and Grocery store type. There will also be a constructor providing the 
ability for passing and setting values for the class attribute, a method called 
sell_item, getters and setters, and the methods calculate_total_sales_tax and 
calculate_total_sales implemented from the abstract class Store
'''

from store import *
class GroceryStore(Store):

    def __init__(self, name, address, availability, sales_tax_percentage, total_revenue, grocery_store_type):
        self.__total_revenue = total_revenue
        self.__grocery_store_type = grocery_store_type
        Store.__init__(self, name, address, availability, sales_tax_percentage)

    def getTotalRevenue(self):
        return(self.__total_revenue)

    def getGroceryStoreType(self):
        return(self.__grocery_store_type)

    def setTotalRevenue(self, total_revenue):
        self.__total_revenue = total_revenue

    def setGroceryStoreType(self, grocery_store_type):
        self.__grocery_store_type = grocery_store_type

    def sell_item(self, quantity, price):
        GroceryStore.setTotalRevenue(self, GroceryStore.getTotalRevenue(self) + (quantity * price))
        return GroceryStore.getTotalRevenue(self)

    def calculate_total_sales_tax(self):
        return(GroceryStore.getTotalRevenue(self) * Store.getSalesTaxPercentage(self))
    
    def calculate_total_sales(self):
        return(GroceryStore.getTotalRevenue(self) + GroceryStore.calculate_total_sales_tax(self))