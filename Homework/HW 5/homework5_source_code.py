'''
Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will take in two files containing data representing
employee count per department and the net profit for a company over the last 10 years.
It will parse that file into lists that will then be used in the creation of several
charts using the matplotlib library.
'''
import os, matplotlib.pyplot as plt

def main():
    f1 = "employee_count_by_department.txt"
    f2 = "last_ten_year_net_profit.txt"

    #Here are the lists we will use for saving all the input from the files
    departments = list()
    numEmployees = list()
    years = list()
    profit = list()
    
    if os.path.isfile(f1): #Checking if that file exists
        infile = open(f1, "r")
        
        titleLine = infile.readline() #we will read the title line of the file
        dataLine = infile.readline()
        while dataLine != "": #While this file has data in it, we'll read it
            tempList = dataLine.split(", ") #splitting the string by the comma
            departments.append(tempList[0].strip()) #removing white space and appending the department name
            numEmployees.append(eval(tempList[1])) #evaluating the employee number as an integer and appending it
            dataLine = infile.readline()
    else:
        print("That file does exist!")

    if os.path.isfile(f2): 
        infile = open(f2, "r")
        
        titleLine = infile.readline()
        dataLine = infile.readline()
        while dataLine != "":
            tempList = dataLine.split(";") #split the string by the ";"
            years.append(eval(tempList[0].strip())) #append the year after removing white space and evaluating it as an int
            #For the profit, we need to strip the white space, remove the comma in the middle of the number, and take everything in the string after the "$" and then evaluate it as an int
            profitTemp = tempList[1].strip().replace(',', '')[1:]
            profit.append(int(profitTemp)) #We can finally add the corrected profit
            dataLine = infile.readline()
    else:
        print("That file does exist!")

    ''' #For debugging purposes
    print(departments)
    print(numEmployees)
    print(years)
    print(profit)
    '''

    plt.pie(numEmployees, labels = departments, autopct='%1.1f%%')
    plt.title("Number of Employees per Department")
    plt.show()

    plt.plot(years, profit)
    plt.title("Profit of Company over 10 years")
    plt.xlabel("Year of Business")
    plt.ylabel("Profit(in dollars, where every '.1' represents 1 million)")
    plt.show()

    plt.bar(years, profit, log = True)
    plt.title("Profit of Company over 10 years")
    plt.xlabel("Year of Business")
    plt.ylabel("Profit(in dollars)")
    plt.show()
    
main();
