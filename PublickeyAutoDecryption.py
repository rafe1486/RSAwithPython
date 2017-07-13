from Crypto.PublicKey.RSA import construct
from OpenSSL import crypto
#from Crypto.Util.number import inverse
import include.key as key
import include.msg as msg
from sys import setrecursionlimit
from sympy import primefactors,totient,mod_inverse
from profilehooks import profile

setrecursionlimit(1000000)

rsaPublicKey = key.importKey('PublicKey.pem')
publicKeySize = rsaPublicKey.size()
print("Public key size :",publicKeySize+1)

"""
        ed = 1 mod phi(n)
        1.find phi(n)
        2.find d
"""

@profile
def decryp():
    n = rsaPublicKey.key.n
    e = rsaPublicKey.key.e
    primeFactor = primefactors(n)
    p = primeFactor[-1]
    q = primeFactor[0]
    phiOfn = totient(n)
    rsakey = construct([n,e,mod_inverse(e, phiOfn),p,q,mod_inverse(p, q)])
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

decryp()