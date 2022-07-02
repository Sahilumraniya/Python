# 1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is.

# This is medthos no 1
"""
firstName=input("Enter Your First Name : ") 
middleName=input("Enter Your Middle Name : ") 
lastName=input("Enter Your Last Name : ")
print(firstName[:1]+"."+middleName[:1]+"."+lastName) 
"""
name=input("Enter Your Full Name : ")
spaceIndex=name.find(" ")
spaceIndex2=name.find(" ",spaceIndex+1)
print(name[:1]+"."+name[spaceIndex+1]+"."+name[spaceIndex2+1:])