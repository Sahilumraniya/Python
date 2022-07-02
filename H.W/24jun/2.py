"""
2. Write a Python recursive function that returns nth term of Fibonacci Sequence.

1, 1, 2, 3, 5, 8, 13

Recursive Definition:
Recursive Step:
nth term = (n-1)th term + (n-2)th term
Non Recursive Step:
1st term = 1
2nd term = 1
"""
def rec_fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return rec_fibo(n-1)+rec_fibo(n-2)

print(rec_fibo(5))