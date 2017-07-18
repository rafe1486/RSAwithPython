from sympy import primefactors
from sympy.physics.quantum.shor import shor
from profilehooks import profile


#@profile
def pfac(n):
    prime = primefactors(n)
    print (prime[-1])
    print (prime[0])


#pfac(3526475443)
#pfac(220358060631995875028749850532080228339)
#shor(3526475443)
print(2**70)
print(10**50)

print(10**100)