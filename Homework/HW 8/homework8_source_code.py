'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will solve two problems. The first problem involves the creation of an array containing the values 1 - 15,
which will then be reshaped into a 3-by-5 array. Indexing and slicing techniques using the NumPy library will then be used to perform the 
following operations:
A) Select row 2
B) Select column 4
C) Select rows 0 and 1
D) Select columns 2-4
E) Select the element that is in row 1 and column 4
F) Select all elements from rows 1 and 2 that are in columns 0, 2, and 4
The Second problem involves loading in a dataset called Student_Grades.csv, and then completing the following requirements:
A) Display all data on screen
B) Determine how many student were in the dataset
C) Display the number of rows and columns of your numpy array
D) Display the array data types
E) Display the following Descriptive statistics of students' overall percentage scores:
    a. Min score
    b. Max score
    c. Mean value
    d. Median
    e. Mode
    f. Standard Deviation
    g. 25% and 75% percentile
F) Determine how many students achieved an A grade, B, C, D, and F grades
G) Create a pie chart based on the above grade achievements
'''
import os, numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy import stats

def main():
    q1()
    q2()

def q1():
    array = np.arange(1, 16, 1)
    array = np.reshape(array, (3, 5))
    print(array) #Print array, for testing purposes
    print("Row 2 of array:", array[1:2]) #Selecting row 2
    print("Column 4 of the array:", array[:, 3]) #Select column 4
    print("Rows 0 and 1 of the array:\n", array[0:2]) #Select rows 0 and 1
    print("Columns 2 - 4 of the array:\n", array[:, 2:5]) #Select columns 2 - 4
    print("Value in row 1 and column 4 of the array:", array[1, 4]) #Selec value at [1, 4]
    print("All elements from rows 1 and 2 that are in columns 0, 2, and 4:\n", array[1:3, [0, 2, 4]])

def q2():
    #data = pd.read_csv("Student_Grades.csv")
    #print(data.to_string())

    #A) Display all data on screen
    data = np.loadtxt(open("Student_Grades.csv", "r"), delimiter = ",", skiprows=1) #Take in data into a numpy array
    print(data)

    #B) Determine how many students were in dataset
    numRows, numColumns = data.shape
    print("Number of students in dataset:", numRows)

    #C) Display the number of rows and columns of your numpy array
    print("Number of rows in dataset:", numRows)
    print("Number of columns in dataset:", numColumns)

    #D) Display the array data types
    print("The array data types are:", data.dtype)

    #Display the following Descriptive statistics of students' overall percentage scores:

    percentages = np.array(data[:, 31])
    #a. Min score
    print("Minimum score:", percentages.min())

    #b. Max score
    print("Maximum score:", percentages.max())

    #c. Mean value
    print("Mean value:", percentages.mean())

    #d. Median
    print("Median:", np.median(percentages))

    #e. Mode
    print("Mode:", stats.mode(percentages))

    #f. Standard Deviation
    print("Standard Deviation:", percentages.std())

    #g. 25% and 75% percentile
    print("25% percentile:", np.percentile(percentages, 25))
    print("75% percentile:", np.percentile(percentages, 75))

    #F) Determine how many students achieved an A grade, B, C, D, and F grades
    print("Number of students with an A:", len(percentages[percentages >= 90]))
    print("Number of students with a B:", len(percentages[np.logical_and(percentages >= 80, percentages < 90)]))
    print("Number of students with a C:", len(percentages[np.logical_and(percentages >= 70, percentages < 80)]))
    print("Number of students with a D:", len(percentages[np.logical_and(percentages >= 60, percentages < 70)]))
    print("Number of students with an F:", len(percentages[percentages <= 59]))

    numGrades = [len(percentages[percentages >= 90]), len(percentages[np.logical_and(percentages >= 80, percentages < 90)]), len(percentages[np.logical_and(percentages >= 70, percentages < 80)]), len(percentages[np.logical_and(percentages >= 60, percentages < 70)]), len(percentages[percentages <= 59])]
    gradeLetters = ["A", "B", "C", "D", "F"]

    plt.pie(numGrades, labels = gradeLetters, autopct = '%1.1f%%')
    plt.title("Student Performance Pie Chart")
    plt.show()

main()