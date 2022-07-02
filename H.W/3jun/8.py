# 8. Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

def armstrong(n):
    l=len(str(n))
    num= [i for i in str(n)]
    s=0
    for i in num:
        s+=int(i)**l
    if s==n:
        return 1
    else:
        return 0

a=int(input("Enter strating number : "))
b=int(input("Enter ending number : "))
ar=[]
for i in range(a,b+1):
   if armstrong(i)==1:
       ar.append(i)
print(ar) 