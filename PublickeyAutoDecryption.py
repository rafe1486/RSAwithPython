from Crypto.PublicKey import RSA
import fractions 
import main
import sys
sys.setrecursionlimit(1000000)


def checksize(keySize, messageSize):
    keySize /=8
    keySize =int(keySize)
    print("Key Size : ",keySize)
    print("Msg Size : ",messageSize)
    if(keySize >= messageSize):
        return True
    if(keySize < messageSize):
        return False

with open('PublicKey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    with open('cipher','rb') as cipherFile:
        ciphertext = cipherFile.read()
    cipherSize = len(ciphertext)
    print("cipherSize :",cipherSize*8)
    print("keySize :",keySize+1)
    #print(dir(rsakey.key))
    #print(dir(rsakey.keydata))

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
            primfac.append(d)  # supposing you want multiple factors repeated
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
            totient -= totient//p # integer division
    return totient

n = rsakey.key.n
e = rsakey.key.e
primeFactor = primes(n)
p = primeFactor[0]
q = primeFactor[1]
phiOfn = totient(n)
def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

d = mulinv(e,phiOfn)
print("e : ",e)
print("d : ",d)
print("n : ",n)
print("p : ",p)
print("q : ",q)
print("phi : ",phiOfn)

with open('FakePrivateKey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    rsakey.key.d = d
    rsakey.key.n = n
    rsakey.key.p = p
    rsakey.key.q = q
    rsakey.key.e = e
    
    print(rsakey.key.u)
    print(dir(rsakey.key))
    with open('cipher','rb') as text_file:
      ciphertext = text_file.read()
    cipherSize = len(ciphertext)
    if (checksize(keySize, cipherSize)):
       text = rsakey.decrypt(ciphertext)
    else:
        keySize +=1
        keySize /=8
        keySize =int(keySize)
        text =b''
        ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
        for ctext in  ciphertext :
            text += rsakey.decrypt(ctext)
        print(text.decode('utf-8', 'ignore'))
