# 1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
"""
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A
"""

n=float(input("Enter Percentage : "))
if n>=75:
    print("Your Grad : A")
elif n>=65:
    print("Your Grad : B")
elif n>=55:
    print("Your Grad : C")
elif n>=45:
    print("Your Grad : D")
elif n>=35:
    print("Your Grad : E")
elif n<35:
    print("Your Grad : F")
else:
    print("You Enter Worng Percrntage rang")