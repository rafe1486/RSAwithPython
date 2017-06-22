from Crypto.PublicKey import RSA
import sys
import main

bits = 32
message = '123456789'
print("msg :",message)

def checksize(keySize, messageSize):
    messageSize *= 8
    keySize += 1
    print("Key Size : ",keySize)
    print("Msg Size : ",messageSize)
    if(keySize >= messageSize):
        return True
    if(keySize < messageSize):
        return False

main.saveKey(main.createKeyPair(bits))
with open('Publickey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    messageSize = len(message)
    message = message.encode()

    if (checksize(keySize, messageSize)):
        ciphertext = rsakey.encrypt(message, 0)[-1]
        print(ciphertext.decode('utf-8', 'ignore'))
        print("ENcryp")
    else:
        keySize +=1
        keySize /=8
        keySize =int(keySize)
        ciphertext =b''
        message = [message[i:i+keySize] for i in range(0, len(message), keySize)]
        for msg in message :
            print("keySize: ",keySize)
            print("msg : ",msg)
            ciphertext += rsakey.encrypt(msg,0)[-1]
            print(ciphertext)
        print("ENcryp")
        print("KeySize < MsgSize")
    #with open('Ciper','w') as text_file:
       # print (ciphertext.decode('UTF-8'),file=text_file)
    print()

with open('PrivateKey.pem', 'rb') as file:
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


"""
with open('Ciper','w') as text_file:
       # print (ciphertext.decode('UTF-8'),file=text_file)
    print()
text = rsakey.decrypt(ciphertext)
  print(text)
    print(text.decode('utf-8', 'ignore'))

    with open('Ciper','rb') as text_file:
        print(ciphertext)
        paintext = cipher.decrypt(ciphertext)
        print(paintext.decode('utf-8', 'ignore'))
"""