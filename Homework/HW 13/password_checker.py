'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will be responsible for checking that the password entered 
meets a pre-defined criteria. A function, does_password_pass_check, will be implemented.
This method will be a recursive function that takes in a string "password",  and checks whether
the password has a digit in it. The function returns true or false based on that.
'''

def main():
    print(does_password_pass_check("161613"))
    print(does_password_pass_check("asdasda"))
    print(does_password_pass_check("1asdasda"))
    print(does_password_pass_check("asdasdasd2asdasdwa"))
    print(does_password_pass_check("asdasdasdasdasdwa1"))

def does_password_pass_check(password):
    if password[0].isdigit():
        return True
    elif len(password) == 1:
        return False
    else:
        return does_password_pass_check(password[1:])

main()