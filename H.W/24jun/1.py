"""
1. Write a Python recursive function that returns nth term of an Geometric Progression.
Geometric Progression:
first term (a) = 3
common ratio (r) = 4

GP: 3, 12, 48, 192, 768.....

200th term: 199th term * r
Recursive Definition:
Recursive Step:
nth term = (n-1)th term * r
Non Recursive Step:
1st term = a
"""
def rec_GP(a,r,n):
    if n == 1:
        return a
    else:
        return r*rec_GP(a,r,n-1)

a=int(input("Enter first term of GP : "))
r=int(input("Enter common ratio of GP : "))
n=int(input("Enter nth term :"))
print("nth term is :",rec_GP(a,r,n))