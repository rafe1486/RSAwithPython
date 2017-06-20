from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

message = b'asdfc'
"""
rsakey = RSA.generate(2048)
print(rsakey.publickey().exportKey().decode('utf-8'))"""


with open('Publickey.pem','r') as privatefile:
    keydata = privatefile.read()
    rsakey = RSA.importKey(keydata)
    cipher = PKCS1_OAEP.new(rsakey.publickey())
    ciphertext = cipher.encrypt(message)
    with open('Ciper','wb') as text_file:
        text_file.write(ciphertext)
    print("ENcryp")
    print(" ")

with open('PrivateKey.pem','rb') as publicfile:
    keydata = publicfile.read()
    rsakey = RSA.importKey(keydata)
    print(rsakey.has_private())
    cipher = PKCS1_OAEP.new(rsakey)
    with open('Ciper','rb') as text_file:
        print(ciphertext)
        paintext = cipher.decrypt(ciphertext)
        print(paintext.decode('utf-8', 'ignore'))