from Crypto.PublicKey import RSA
import main

def checksize(keySize, messageSize):
    keySize /=8
    keySize =int(keySize)
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
    with open('cipher','rb') as cipherFile:
        ciphertext = cipherFile.read()
    cipherSize = len(ciphertext)
    print("cipherSize :",cipherSize*8)
    print("keySize :",keySize+1)
    print("e :",rsakey.key.e)
    print("n :",rsakey.key.n)
    print(dir(rsakey.key))
    print(dir(rsakey.keydata))
    for a in rsakey.keydata.pop():
        print(a)
    

    """
        
        ed = 1 mod phi(n)
        1.find phi(n)
        2.find d
    """


    """if (checksize(keySize, cipherSize)):
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