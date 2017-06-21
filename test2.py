from Crypto.PublicKey import RSA
import sys
message = b'asdfc'
"""
rsakey = RSA.generate(2048)
print(rsakey.publickey().exportKey().decode('utf-8'))"""

def checksize(size1,size2):
    size2 += 2
    if(size1 >= size2):
        return "size1>=size2"
    if(size1 <  size2):
        return "size1>size2"
    
with open('Publickey.pem','r') as privatefile:
    keydata = privatefile.read()
    rsakey = RSA.importKey(keydata)
    print(sys.getsizeof(message))
    ciphertext = rsakey.encrypt(message,0)
    print(ciphertext[-1].decode('utf-8','ignore'))
    print()
    #with open('Ciper','w') as text_file:
       # print (ciphertext.decode('UTF-8'),file=text_file)
    print("ENcryp")
    print(" ")

with open('PrivateKey.pem','r') as publicfile:
    keydata = publicfile.read()
    rsakey = RSA.importKey(keydata)
    text = rsakey.decrypt(ciphertext)
    print(text)
    print(text.decode('utf-8','ignore'))
"""
    with open('Ciper','rb') as text_file:
        print(ciphertext)
        paintext = cipher.decrypt(ciphertext)
        print(paintext.decode('utf-8', 'ignore'))
"""