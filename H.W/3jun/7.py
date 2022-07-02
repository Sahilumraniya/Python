# 7. Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.

def prime(n):
    """This faunction is find the given number is prime or not"""
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

a=int(input("Enter strating number : "))
b=int(input("Enter ending number : "))
p=[]
for i in range(a,b+1):
   if prime(i)==1:
       p.append(i)
print(p) 