'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will utilize the pickle library and dictionaries to record, retrieve, and edit company records
consisting of a User's name and email. The program will offer users a menu with options to choose from, which includes:
    1) Add a new name and email address.
    2. Find an existing email address from a name.
    3. Change an existing email address.
    4. Delete an existing name and email address.
    5. Exit the program
The program itself will run continously until option 5 is chosen. At the start and end of the program, the information will be
unbinded and binded into a text file, respectively.
'''

import pickle, os

def userInput():
    print('''
    Welcome. Enter the number corresponding to what you'd like to do.

    1. Add a new name and email address.
    2. Find an existing email address from a name.
    3. Change an existing email address.
    4. Delete an existing name and email address.
    5. Exit the program
    ''')
    choice = eval(input('Enter a number: '))
    return choice

def addUser(companyRecords):
    name = input("Enter the name you would like to add: ")
    email = input("Enter the email you would like to add: ")
    companyRecords[name] = email
    print("User added")

def findEmail(companyRecords):
    name = input("Enter the name you would like to search: ")
    if name in companyRecords:
        print("The email is:", companyRecords[name])
    else:
        print("There is no such user!")

def changeEmail(companyRecords):
    name = input("Enter the name of the email you would like to change: ")
    if name in companyRecords:
        email = input("Enter the new email you would like to use: ")
        companyRecords[name] = email
        print("User email updated")
    else:
        print("There is no such user!")

def deleteUser(companyRecords):
    name = input("Enter the name of the user you want to delete: ")
    if name in companyRecords:
        del companyRecords[name]
        print("User deleted")
    else:
        print("There is no such user!")

def main():

    if os.stat("CompanyRecords.txt").st_size != 0:
        print("Not empty file")
        companyRecords = pickle.load(open("CompanyRecords.txt", "rb"))
    else: 
        companyRecords = dict()

    
    choice = userInput()

    while choice != 5:
        if choice == 1:
            addUser(companyRecords)
        elif choice == 2:
            findEmail(companyRecords)
        elif choice == 3:
            changeEmail(companyRecords)
        elif choice == 4:
            deleteUser(companyRecords)
        else:
            print('That is not a valid option!')

        choice = userInput()

    pickle.dump(companyRecords, open("CompanyRecords.txt", "wb"))

main()