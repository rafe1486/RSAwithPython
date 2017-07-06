import include.key as key
import include.msg  as msg
import Crypto.Util.number as number
import random
import fastMod
import gmpy2

bits = 32
messages = 'ABCD'
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
    ciphertext += str(fastMod.pow_mod(msgtoDec, rsakey.key.e, rsakey.key.n))+" "

print("ciphertext is :",ciphertext)

"""chosen cipher text"""
def randomR(bits, n):
    """
    random R between 1 - e and R is relative prime with n
    """
    num = random.randint(1, n)
    while(number.GCD(num, rsakey.key.n) != 1):
        num = random.randint(1, n)
    return num

r = randomR(bits, rsakey.key.e)
print("r is: ", r)

"""Times cipher by r**e % n"""
ciphertext = ciphertext.split(" ")
newciphertext = ""
for ctext in ciphertext :
    if ctext != '':
        ctext = int(ctext)
        newciphertext += str((ctext*fastMod.pow_mod(r, rsakey.key.e, rsakey.key.n)))+" "
ciphertext = newciphertext
print("cipher times r :", ciphertext)

"""Decryp with PrivateKey"""
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

"""Devide decryp message by r"""
text = text.split(" ")
messages=""
for message in text :
    if message != '':
        message = int(message)/r
        messages += msg.dectoMsg(message,rsakey)
print("msg :", messages)