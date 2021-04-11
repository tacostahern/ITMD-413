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
    print("Price per person: $", elCid.getPricePerPerson())
    print("Total sales tax: $", elCid.calculate_total_sales_tax())
    print("Total sales: $", elCid.calculate_total_sales())

    print()
    print(wholeFoods.getName(), "statistics:")
    print("Address:", wholeFoods.getAddress())
    print("Store open?", wholeFoods.is_store_open())
    print("Sales tax percentage: ", wholeFoods.getSalesTaxPercentage() * 100, "%")
    print("Total revenue: $", wholeFoods.getTotalRevenue())
    print("Grocery store type:", wholeFoods.getGroceryStoreType())
    print("Total sales tax: $", wholeFoods.calculate_total_sales_tax())
    print("Total sales: $", wholeFoods.calculate_total_sales())

    print()
    print("El Cid new patrons: 20")
    elCid.seat_patrons(20)
    print("New current occupancy:", elCid.getCurrentOccupancy())

    print()
    print("El Cid new patrons: 100")
    elCid.seat_patrons(100)
    print("New current occupancy:", elCid.getCurrentOccupancy())
    elCid.serve_patrons(20)
    print("Current Occupancy:", elCid.checkout_patrons(10))
    print()
    print(elCid.getName(), "updated stats:")
    print("Number of people served:", elCid.getPeopleServed())
    print("Max occupancy:", elCid.getMaxOccupancy())
    print("Current occupancy:", elCid.getCurrentOccupancy())
    print("Price per person: $", elCid.getPricePerPerson())
    print("Total sales tax: $", elCid.calculate_total_sales_tax())
    print("Total sales: $", elCid.calculate_total_sales())

    print()
    print("20 bananas sold at a dollar each")
    print("Whole foods total revenue: $", wholeFoods.sell_item(20, 1))
    print("100 cartons of milk sold at 3 dollars each")
    print("Whole foods total revenue: $", wholeFoods.sell_item(100, 3))
    print()
    print(wholeFoods.getName(), "updated stats:")
    print("Total sales tax: $", wholeFoods.calculate_total_sales_tax())
    print("Total sales: $", wholeFoods.calculate_total_sales())
main()
