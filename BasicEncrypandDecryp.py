from Crypto.PublicKey import RSA
import main

bits = 64
message = '123456789'
print("msg :",message)

def checksize(keySize, messageSize):
    keySize +=1
    keySize /=8
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
    else:
        keySize +=1
        keySize /=8
        keySize =int(keySize)
        ciphertext =b''
        message = [message[i:i+keySize] for i in range(0, len(message), keySize)]
        for msg in message :
            ciphertext+=rsakey.encrypt(msg,0)[-1]
            
    with open('cipher','wb') as text_file:
       text_file.write(ciphertext)
    print()

with open('PrivateKey.pem', 'rb') as file:
    keydata = file.read()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    with open('cipher','rb') as text_file:
      ciphertext = text_file.read()
    cipherSize = len(ciphertext)
    if (checksize(keySize, cipherSize)):
       text = rsakey.decrypt(ciphertext)
    else:
        keySize +=1
        keySize /=8
        keySize =int(keySize)
        text =b''
        ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
        for ctext in  ciphertext :
            text += rsakey.decrypt(ctext)
        print(text.decode('utf-8', 'ignore'))