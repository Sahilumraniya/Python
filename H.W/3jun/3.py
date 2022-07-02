# 3. Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in ex-1 to find factorial of each one of them and using average function prints the average of factorials of them.

def avg_five(a,b,c,d,e):
    """Thsi faunction find average of five number"""
    return (a+b+c+d+e)/5

def factorial(n):
    """this faunction find factorial of given number in arrgument"""
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

n1=int(input("Enter number : "))
n2=int(input("Enter number : "))
n3=int(input("Enter number : "))
n4=int(input("Enter number : "))
n5=int(input("Enter number : "))

print("Average of factorial number : ",avg_five(factorial(n1), factorial(n2), factorial(n3), factorial(n4), factorial(n5)))