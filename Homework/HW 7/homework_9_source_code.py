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

    for i in infoLine:
        temp = i.split(":")
        print("dn:", temp[0] + ",", "dc=gmail, dc=com")
        print("cn:", temp[1], temp[2])
        print("sn:", temp[2])
        print("telephoneNumber:", temp[3])

def readFile():
    file = "information.txt"

    if os.path.isfile(file):
        infile = open(file, "r")
        return infile

def getInfo(infile):
    infoLine = list()

    dataLine = infile.readline()

    while dataLine != "":
        infoLine.append(dataLine)
        dataLine = infile.readline()

    return infoLine

main()