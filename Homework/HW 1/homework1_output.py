Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py
Enter the number of students: 3
Enter a student name: Tony
Enter a student score: 100
Enter a student name: Eric
Enter a student score: 50
Top two students:
Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py", line 33, in <module>
    print(student + "'s score is " + str(score1))
NameError: name 'student' is not defined
>>> 
= RESTART: C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py
Enter the number of students: Tony
Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py", line 4, in <module>
    numberOfStudents = eval(input("Enter the number of students: "))
  File "<string>", line 1, in <module>
NameError: name 'Tony' is not defined
>>> 
= RESTART: C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py
Enter the number of students: 3
Enter a student name: Tony
Enter a student score: 100
Enter a student name: Eric
Enter a student score: 50
Enter a student name: Anthony
Enter a student score: 0
Top two students:
Anthony's score is 100
Eric's score is 50
>>> 
= RESTART: C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py
Enter the number of students: 3
Enter a student name: Tony
Enter a student score: 100
Enter a student name: Eric
Enter a student score: 50
Enter a student name: Anthony
Enter a student score: 0
Top two students:
Tony's score is 100
Eric's score is 50
>>> 
= RESTART: C:\Users\tacos\Documents\ITMD 413\Homework\HW 1\homework1_source_code.py
Enter the number of students: 5
Enter a student name: a
Enter a student score: 100
Enter a student name: b
Enter a student score: 25
Enter a student name: c
Enter a student score: 50
Enter a student name: d
Enter a student score: 500
Enter a student name: e
Enter a student score: 0
Top two students:
d's score is 500
a's score is 100
>>> 