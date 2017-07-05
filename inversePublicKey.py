import include.key as key
import include.msg  as msg
import Crypto.Util.number as number
import random
import math
import fastMod

bits = 32
messages = 'ABCD'
print("msg :", messages)

"""Generate Key """
key.saveKey(key.createKeyPair(bits))

"""Encryp with Publickey"""
rsakey = key.importKey('PublicKey.pem')
keyLength = key.getHalfofKeyLength(rsakey)
messageLength = msg.getLength(messages)

messages = [messages[i:i+keyLength] for i in range(0, messageLength, keyLength)]
ciphertext = ""
for message in messages :
    msgtoDec = msg.msgtoDec(message)
    ciphertext += str(fastMod.pow_mod(msgtoDec, rsakey.key.e, rsakey.key.n))+" "

print("ciphertext is :",ciphertext)

def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

"""Decryp with PrivateKey"""
rsakey = key.importKey('PrivateKey.pem')
keyLength = key.getHalfofKeyLength(rsakey)
ciphertext = ciphertext.split(" ")
text = ""
for ctext in ciphertext :
    if ctext != '':
        ctext = int(ctext)
        p = (rsakey.key.e)
        c = (ctext)
        print(p)
        print(rsakey.key.n)
        print(c)
        text += str(iroot(c,p))+" "
        print(text)
decryptext = text.split(" ")
stringText = ""
for strtext in decryptext :
    if strtext != '':
        strtext = int(strtext)
        stringText += msg.dectoMsg(strtext,rsakey)
print("msg after decryp (String format) :", stringText)