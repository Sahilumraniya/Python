# 1. Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.

def factorial(n):
    """this faction find factorial of given number in arrgument"""
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact


a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = int(input("Enter number : "))
d = int(input("Enter number : "))
f = int(input("Enter number : "))

print(f"{a}! = ", factorial(a))
print(f"{b}! = ", factorial(b))
print(f"{c}! = ", factorial(c))
print(f"{d}! = ", factorial(d))
print(f"{f}! = ", factorial(f))
print(f"{a}! + {b}! + {c}! + {d}! + {f}! = ", factorial(a) +
      factorial(b)+factorial(c)+factorial(d)+factorial(f))
