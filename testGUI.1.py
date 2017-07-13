from sympy import primefactors
from profilehooks import profile


@profile
def pfac(n):
    prime = primefactors(n)
    print (prime[-1])
    print (prime[0])


#pfac(3526475443)
pfac(220358060631995875028749850532080228339)