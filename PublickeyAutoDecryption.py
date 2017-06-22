from Crypto.PublicKey import RSA
import sys
import main

bits = 32

def checksize(keySize, messageSize):
    messageSize *= 8
    keySize += 1
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
    cipherSize = len(ciphertext)

    if (checksize(keySize, cipherSize)):
       text = rsakey.decrypt(ciphertext)
       print(text.decode('utf-8', 'ignore'))
       print("DEcryp")
    else:
        print("KeySize < MsgSize")
        keySize +=1
        keySize /=8
        keySize =int(keySize)
        text =b''
        ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
        for ctext in  ciphertext :
            print (ctext)
            text += rsakey.decrypt(ctext)
        print(text.decode('utf-8', 'ignore'))
