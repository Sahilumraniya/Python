"""4. Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d"""

def nth_term_ap(a,d,n):
    """This faunction find nth term of sreais"""
    return a+(n-1)*d

a=int(input("Enter first term of series : "))
d=int(input("Enter difference of series : "))
tn=int(input("Enter term number which you want to print : "))
an=[]
"""print("An = ",nth_term_ap(a, d, 1))
for i in range(2,tn+1):
    print(" , ",nth_term_ap(a, d, i))
"""
for i in range(1,tn+1):
    an.append(nth_term_ap(a,d,i))
print(an)