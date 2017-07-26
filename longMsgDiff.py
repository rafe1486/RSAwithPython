import include.key as imkey
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

bits = 1024

#imkey.saveKey(imkey.createKeyPair(bits))
key = imkey.importKey('PublicKey.pem')

message = b'A'
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)

print(ciphertext,"\n")
print("lenght of cipher text :",len(ciphertext),"\n")
#print(ciphertext.decode('utf-8', 'ignore'))

key = imkey.importKey('PrivateKey.pem')
cipher = PKCS1_OAEP.new(key)
text = cipher.decrypt(ciphertext)
print(text,"\n")