import include.key as key
import include.msg  as msg
import Crypto.Util.number as number
import random
import fastMod
import math
import gmpy2

bits = 1024
messages = 'A'
print("msg :", messages)

"""Generate Key """
#key.saveKey(key.createKeyPair(bits))

"""Encryp with Publickey"""
rsakey = key.importKey('PublicKey.pem')
keyLength = key.getHalfofKeyLength(rsakey)
messageLength = msg.getLength(messages)

messages = [messages[i:i+keyLength] for i in range(0, messageLength, keyLength)]
ciphertext = ""
for message in messages :
    msgtoDec = msg.msgtoDec(message)
    print("msgtoDex is :",msgtoDec)
    rsakey.key.e = 3
    ciphertext += str(fastMod.pow_mod(msgtoDec, rsakey.key.e, rsakey.key.n))+" "

print("ciphertext is :",ciphertext)
print("M**e is :",msgtoDec**rsakey.key.e)
print("rsakey.key.e : ",rsakey.key.e)
print("rsakey.key.n : ",rsakey.key.n)
strtext = int(10**(math.log10(int(ciphertext))/rsakey.key.e))
#print(10**(math.log10(int(ciphertext))/rsakey.key.e))
msg = strtext.to_bytes(key.getKeyLength(rsakey), byteorder="little").decode("utf-8","ignore")
print("msg : ",msg)


"""Decryp with PrivateKey
rsakey = key.importKey('PrivateKey.pem')
keyLength = key.getHalfofKeyLength(rsakey)
ciphertext = ciphertext.split(" ")
text = ""
for ctext in ciphertext :
    if ctext != '':
        ctext = int(ctext)
        text += str((fastMod.pow_mod(ctext, rsakey.key.d, rsakey.key.n)))+" "
print("msg after decryp (int format) :", text)
decryptext = text.split(" ")
stringText = ""
for strtext in decryptext :
    if strtext != '':
        strtext = int(strtext)
        #print(strtext.to_bytes(key.getKeyLength(rsakey), byteorder="little"))
        stringText += strtext.to_bytes(key.getKeyLength(rsakey), byteorder="little").decode("utf-8","ignore")
print("msg after decryp (String format) :", stringText)
"""