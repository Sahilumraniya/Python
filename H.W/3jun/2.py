# 2. Write a Python function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.

def prime(n):
    """This faunction find the number given by arrgument is prime or not"""
    p=0
    for i in range(2,n):
        if n%i==0:
            p=0
            break
        else:
            p=1
    if p==1:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

num=int(input("Enter number : "))
prime(num)