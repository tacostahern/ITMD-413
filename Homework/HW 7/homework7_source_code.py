'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will solve two problems. Firstly, it will take in a file containing a few lines of information 
consisting of the following information: "Username:Firstname:Lastname:Telephone number". It will then convert this information into
a LDAP record format, formatted as follows:

    dn: uid=Username, dc=example, dc=com
    cn : Firstname Lastname
    sn: Lastname
    telephoneNumber: Telephone number

For the second problem, the program will take in user input of however many phone numbers they want, and in turn it will be able to 
tell if the phone numbers are valid based on the input.
'''

import re, os

def main():
    file = readFile()
    infoLine = getInfo(file)

    #for i in infoLine:
        #print(i)

    for i in infoLine: #Using the list we got from getInfo, we go line by line and print out the formatted information, after saving that in its own list
        temp = i.split(":")
        print("dn:", temp[0] + ",", "dc=gmail, dc=com")
        print("cn:", temp[1], temp[2])
        print("sn:", temp[2])
        print("telephoneNumber:", temp[3])


    phoneNumber()

def readFile(): #This method gets the file we read and returns the readable file
    file = "information.txt"

    if os.path.isfile(file):
        infile = open(file, "r")
        return infile

def getInfo(infile): #This method takes our readable file and saves the data in a list, then returns that list
    infoLine = list()

    dataLine = infile.readline()

    while dataLine != "":
        infoLine.append(dataLine)
        dataLine = infile.readline()

    return infoLine

def phoneNumber(): #This method solves question 2
    
    #pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

    goAgain = input("Please enter 'Y' to enter a phone number, or enter anything else to stop: ")

    while goAgain.lower() == 'y':

        pattern = re.compile(r'''(
        (\()? #Optional first opening parenthesis for area code
        (\d{3}) #should be 3 digits for area code
        (\s|\)|-|\)\s)? #The next symbol can be a space, closing parenthesis, hypen, or parenthesis with space
        (\d{3})#Need 3 digits for the rest of the number
        (\s|-)?#There can be another optional space or hypen
        (\d{4})#Final four digits of number
        )''', re.VERBOSE)
        userInput = input("Please enter the phone number: ")

        match = re.fullmatch(pattern, userInput) #Matches the full entered string to our pattern
        if match != None: #If we do get a match
            pnList = list(userInput)#We convert the string to a list, so we can format it more easily
            for i in userInput:
                if i.isdigit() == False:#remove non digit characters from the number
                    pnList.remove(i)
            
            print("The formatted number is (" + pnList[0] + pnList[1] + pnList[2] +  #Used to format the number simply
            ")", pnList[3] + pnList[4] + pnList[5], 
            pnList[6] + pnList[7] + pnList[8] + pnList[9])
            
        else:
            print("That is not a valid phone number")

        goAgain = input("Please enter 'Y' to enter a phone number, or enter anything else to stop: ")

    
main()