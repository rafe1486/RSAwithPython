from Crypto.PublicKey import RSA
import main
import Crypto.Util.number as number
import fastMod

bits = 32
message = 'ABCD'
print("msg :",message)
#main.saveKey(main.createKeyPair(bits))
def checksize(keySize, messageSize):
    keySize +=1
    keySize /=8
    if(keySize >= messageSize):
        return True
    if(keySize < messageSize):
        return False

with open('PublicKey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    messageSize = len(message)
    message = message.encode()
    msgto_byte = int.from_bytes(message,byteorder="little")
    print("msgtobyte",msgto_byte)
    ciphertext = fastMod.pow_mod(msgto_byte,rsakey.key.e,rsakey.key.n)
    print("cipher after Encryp",ciphertext)


"""cipher"""

r = 3
print("r is: ",r)
ciphertext = ciphertext*fastMod.pow_mod(r,rsakey.key.e,rsakey.key.n)
print("cipher times r",ciphertext)


with open('PrivateKey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    text = fastMod.pow_mod(ciphertext,rsakey.key.d,rsakey.key.n)
    #text = int(text)
    print("cipher after decrypt",text)
    text = text/r
    print("cipher after devide by r",text)
    text = int(text)
    print("cipher after cast to int",text)
    text = text.to_bytes(text.bit_length(), byteorder="little")
    print("textbyte",text)
    print("decryp",text.decode('utf-8', 'ignore'))

"""Show Debug"""
print("rsakey.key.e : ",rsakey.key.e)
print("rsakey.key.d : ",rsakey.key.d)
print("rsakey.key.n : ",rsakey.key.n)
print("rsakey.key.p : ",rsakey.key.p)
print("rsakey.key.q : ",rsakey.key.q)
print("rsakey.key.u : ",rsakey.key.u)
