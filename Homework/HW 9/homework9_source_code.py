'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will solve two questions. The first question involves 2 parts: First, the creation of several series
using the pandas library as well as functions performed on them based on the following tasks:
    a. Create a Series from the list [7, 11, 13, 17].
    b. Create a Series with five elements that are all 100.0.
    c. Create a Series with 20 elements that are all random numbers in the 
    range 0 to 100. Use method describe to produce the Series’ basic descriptive 
    statistics.
    d. Create a Series called temperatures of the floating-point 
    values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify 
    the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
    e. Form a dictionary from the names and values in Part (d), then use it to initialize 
    a Series.
Second, the creation of several dataframes using the pandas library as well as the functions performed on them based on the following tasks:
    f. Create a DataFrame named temperatures from a dictionary of three temperature 
    readings each for 'Maxine', 'James' and 'Amanda'.
    g. Recreate the DataFrame temperatures in Part (a) with custom indices using 
    the index keyword argument and a list 
    containing 'Morning', 'Afternoon' and 'Evening'.
    h. Select from temperatures the column of temperature readings for 'Maxine'.
    i. Select from temperatures the row of 'Morning' temperature readings.
    j. Select from temperatures the rows for 'Morning' and 'Evening'temperature 
    readings.
    k. Select from temperatures the columns of temperature readings 
    for 'Amanda' and 'Maxine'.
    l. Select from temperatures the elements for 'Amanda' and 'Maxine' in 
    the 'Morning' and 'Afternoon'.
    m. Use the describe method to produce temperatures’ descriptive statistics.
    n. Transpose temperatures.
    o. Sort temperatures so that its column names are in alphabetical order
The second question involves the titanic.csv dataset, in which we will create a program to explore and mine for the following information: 
    a) How many passengers were in the titanic?
    b) How many male and female passengers were in the titanic?
    c) What was the average age of all passengers?
    d) How many passengers under 21 years of age?
    e) How many survived and how many did not? How many males and how many females?
    f) What was the youngest age that survived, and the oldest age? What were their names.
    g) Display the name of all passengers that survived.
'''
import pandas as pd, numpy as np

def main():
    q1part1()
    q1part2()
    q2()

def q1part1():
    a = pd.Series([7, 11, 13, 17]) #Answer to a
    b = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0]) #Answer to b
    c = pd.Series(np.random.randint(101, size = 20)) #Answer to c, along with the line below it
    print(c.describe())
    temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea']) #Answer to d
    #Answer to e is as follows:s
    dictionary = {
        'Julie': 98.6,
        'Charlie': 98.9,
        'Sam': 100.2,
        'Andrea': 97.9
    }
    e = pd.Series(dictionary)

def q1part2():
    #Answer to f as follows:
    dictionary = {
        'Maxine': [98.9, 96.8, 98.6],
        'James': [68.7, 99.1, 86.3],
        'Amanda': [100.3, 103.5, 93.9]
    }

    temperatures = pd.DataFrame.from_dict(dictionary)
    temperatures = pd.DataFrame(dictionary, index= ['Morning', 'Afternoon', 'Evening']) #Answer to g
    #print(temperatures)
    MaxineTemps = temperatures['Maxine'] #Answer to h
    print(MaxineTemps)
    morningTemps = temperatures.loc[['Morning'], :] #Answer to i
    print(morningTemps)
    mornEveTemps = temperatures.loc[['Morning', 'Evening'], :] #Answer to j
    print(mornEveTemps)
    amandaMaxineTemps = temperatures.loc[:, ['Amanda', 'Maxine']] #Answer to k
    print(amandaMaxineTemps)
    amandaMaxineMornNoonTemps = temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']] #Answer to l
    print(amandaMaxineMornNoonTemps)
    print(temperatures.describe()) #Answer to m
    transposedTemp = temperatures.T #Answer to n
    print(transposedTemp)
    temperatures = temperatures.reindex(sorted(temperatures.columns), axis = 1) #Answer to o
    print(temperatures)
    
def q2():
    pass

main()