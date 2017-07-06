from Crypto.PublicKey import RSA
from OpenSSL import crypto
from Crypto.Util.number import inverse
import include.key as key
import include.msg as msg
import sys
sys.setrecursionlimit(1000000)

rsaPublicKey = key.importKey('PublicKey.pem')
publicKeySize = rsaPublicKey.size()
print("Public key size :",publicKeySize+1)

"""
        ed = 1 mod phi(n)
        1.find phi(n)
        2.find d
"""
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def totient(n):
    unique = []
    totient = n
    for p in primes(n):
        if p not in unique:
            unique.append(p)
            totient -= totient//p
    return totient

n = rsaPublicKey.key.n
e = rsaPublicKey.key.e
primeFactor = primes(n)
p = primeFactor[1]
q = primeFactor[0]
phiOfn = totient(n)

rsakey = RSA.construct([n,e,inverse(e, phiOfn),p,q,inverse(p, q)])
keySize = rsakey.size()


print("rsakey.key.e : ",rsakey.key.e)
print("rsakey.key.d : ",rsakey.key.d)
print("rsakey.key.n : ",rsakey.key.n)
print("rsakey.key.p : ",rsakey.key.p)
print("rsakey.key.q : ",rsakey.key.q)
print("rsakey.key.u : ",rsakey.key.u)

with open('cipher','rb') as text_file:
    ciphertext = text_file.read()
    cipherSize = len(ciphertext)
if (msg.checkSize(rsakey, cipherSize)):
    text = rsakey.decrypt(ciphertext)
    print(text.decode('utf-8', 'ignore'))
else:
    keySize +=1
    keySize /=8
    keySize =int(keySize)
    text =b''
    ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
    for ctext in  ciphertext :
        text += rsakey.decrypt(ctext)
    print(text.decode('utf-8', 'ignore'))

print("Key Size :",keySize*8)
print("Cipher Size :",cipherSize*8)