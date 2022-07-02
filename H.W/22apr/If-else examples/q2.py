# 2. Write a Python program to find whether a given year is a leap year or not. 

year=int(input("Enter Year"))
if year%4==0:
    if year%100==0:
        if year%400==0: print(f"{year} is a leap year")
        else: print(f"{year} is not a leap year")
    else : print(f"{year} is a leap year")
else: print(f"{year} is not a leap year")
