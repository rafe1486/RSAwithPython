import include.key as key
import include.msg  as msg
import Crypto.Util.number as number
import random
import fastMod

bits = 32
messages = 'ABCD'
print("msg :", messages)

"""Generate Key """
key.saveKey(key.createKeyPair(bits))

rsakey = key.importKey('PublicKey.pem')
keySize = key.getKeySize(rsakey)
keyLength = key.getHalfofKeyLength(rsakey)
messageLength = msg.getLength(messages)

print("Key Size :",keySize)
print("Key Length :",keyLength)
print("Msg Length :",messageLength)

messages = [messages[i:i+keyLength] for i in range(0, messageLength, keyLength)]
ciphertext = ""
for message in messages :
    msgtoDec = msg.msgtoDec(message)
    ciphertext += str(fastMod.pow_mod(msgtoDec, rsakey.key.e, rsakey.key.n))+" "
print(ciphertext)
# msgtoDec = msg.msgtoDec(message)
# print("msgtohex", msgtoDec)

# ciphertext = fastMod.pow_mod(msgtoDec, rsakey.key.e, rsakey.key.n)
# print("cipher after Encryp", ciphertext)


# """chosen cipher text"""


# def randomR(bits, n):
#     num = random.randint(1, n)
#     while(number.GCD(num, rsakey.key.n) == 1):
#         num = random.randint(1, n)
#     return num


# r = randomR(bits, rsakey.key.e)
# print("r is: ", r)

# ciphertext = ciphertext * fastMod.pow_mod(r, rsakey.key.e, rsakey.key.n)
# print("cipher times r", ciphertext)


# rsakey = key.importKey('PrivateKey.pem')

# keySize = key.getKeySize(rsakey)

# text = fastMod.pow_mod(ciphertext, rsakey.key.d, rsakey.key.n)
# print("cipher after decrypt", text)
# text = text / r
# print("cipher after devide by r", text)
# text = msg.dectoMsg(text, rsakey)
# print("decryp", text.decode('utf-8', 'ignore'))

# """Show Debug
# print("Key Size :",keySize)
# #print("Cipher Size :",cipherSize)
# print("rsakey.key.e : ",rsakey.key.e)
# print("rsakey.key.d : ",rsakey.key.d)
# print("rsakey.key.n : ",rsakey.key.n)
# print("rsakey.key.p : ",rsakey.key.p)
# print("rsakey.key.q : ",rsakey.key.q)
# print("rsakey.key.u : ",rsakey.key.u)
# """
