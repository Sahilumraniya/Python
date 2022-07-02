# 3.  Write a Python code that prints the index numbers of all the occurrences of "o" in a given string of length 5.

str=input("Enter String : ")
i=0
while i<5:
    if str[i]=="o":
        print(i)
    i+=1