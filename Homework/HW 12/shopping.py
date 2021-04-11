'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will serve as the tester file, making use of the
Restaurant and GroceryStore classes and their respective methods to simulate the
actions that take place in real life restaurants and grocery store.
'''
from restaurant import *
from grocery_store import *

def main():
    elCid = Restaurant("El Cid", "2645 N. Kedzie", "open", .10, 20, 100, 10, 15)
    wholeFoods = GroceryStore("Whole Foods", "959 W Fullerton Ave", "closed", .05, 10000, "Grocery")

    print(elCid.getName(), "statistics:")
    print("Address:", elCid.getAddress())
    print("Store open?", elCid.is_store_open())
    print("Sales tax percentage: ", elCid.getSalesTaxPercentage() * 100, "%")
    print("Number of people served:", elCid.getPeopleServed())
    print("Max occupancy:", elCid.getMaxOccupancy())
    print("Current occupancy:", elCid.getCurrentOccupancy())
    print("Price per person:", elCid.getPricePerPerson())
    print("Total sales tax:", elCid.calculate_total_sales_tax())
    print("Total sales:", elCid.calculate_total_sales())

main()
