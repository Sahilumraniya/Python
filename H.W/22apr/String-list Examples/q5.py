# 5. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".

str=input("Enter String : ")
print(str.replace(" ", "_",1)[::-1].replace(" ", "#",1)[::-1])
