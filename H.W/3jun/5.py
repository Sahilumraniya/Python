# 5. Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

def nth_term_gp(a,r,n):
    return a*(r**(n-1))

a=int(input("Enter first term of series : "))
r=int(input("Enter ratio of series : "))
tn=int(input("Enter term number which you want to print : "))
gp=[]
for i in range(1,tn+1):
    gp.append(nth_term_gp(a,r,i))
print(gp)