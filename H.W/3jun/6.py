# 6. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

def perfect(n):
    """This faunction find the given number is perfect or not"""
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return n
    else:
        return 0
a=int(input("Enter strating point : "))
b=int(input("Enter Ending point : "))
pt=[]
for i in range(a,b+1):
    if perfect(i)!=0:
        pt.append(i)
print(pt)