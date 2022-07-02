def nth_term(a,d,n):
    """
    this function retrun the nth term of ap which first argument is firt term and second argument is common diffrent d and nth term
    """
    if n == 1:
        return a
    else:
        return d+nth_term(a,d,n-1)

print(nth_term(3,4,4))