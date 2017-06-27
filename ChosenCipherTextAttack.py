from Crypto.PublicKey import RSA
import main
import Crypto.Util.number as number

bits = 32
message = '10'
print("msg :",message)

def checksize(keySize, messageSize):
    keySize +=1
    keySize /=8
    if(keySize >= messageSize):
        return True
    if(keySize < messageSize):
        return False

#main.saveKey(main.createKeyPair(bits))
with open('PublicKey.pem', 'rb') as file:
    keydata = file.read()
    file.close()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    messageSize = len(message)
    message = message.encode()
    ciphertext = int.from_bytes(message,byteorder="little")
    ciphertext = ciphertext**rsakey.key.e % rsakey.key.n

            
    with open('cipher','w') as text_file:
       print(ciphertext,file=text_file)
       text_file.close()
    print()

"""Start Attack"""
r = 3
print("r is: ",r)

with open('cipher','r') as text_file:
    ciphertext = text_file.read()
print("ciphertext :",ciphertext)
ciphertext = int(ciphertext)
print("ciphertext :",ciphertext)
text = ciphertext*( (r**rsakey.key.e) % rsakey.key.n)
print(text)
with open('cipher','w') as text_file:
    print(text,file=text_file)
    text_file.close()
    print("write cipher")
"""if (checksize(keySize, cipherSize)):
    text = ciphertext*r
    #print(text.decode('utf-8', 'ignore'))
else:
    keySize +=1
    keySize /=8
    keySize =int(keySize)
    text =b''
    ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
    for ctext in  ciphertext :
        text += ctext*r
    #print(text.decode('utf-8', 'ignore'))
    """

"""Decrypt"""
with open('PrivateKey.pem', 'rb') as file:
    keydata = file.read()
    file.close()
    rsakey = RSA.importKey(keydata)
    keySize = rsakey.size()
    with open('cipher','r') as text_file:
      ciphertext = text_file.read()
    cipherSize = len(ciphertext)
    print(ciphertext)
    ciphertext = int(ciphertext)
    byteArray = ciphertext.to_bytes(ciphertext.bit_length(), byteorder="little")
    text = rsakey.decrypt(byteArray)
       #print(text.decode('utf-8', 'ignore'))


"""Decrypt by devide r"""
print(text)
print(r)
text = int.from_bytes(text,byteorder="little")
print(text)
text /= r
print(text)
text = int(text).to_bytes(ciphertext.bit_length(), byteorder="little")
print(text)
print(text.decode('utf-8', 'ignore'))
"""Show Debug
print("Key Size :",keySize)
print("Cipher Size :",cipherSize)
print("rsakey.key.e : ",rsakey.key.e)
print("rsakey.key.d : ",rsakey.key.d)
print("rsakey.key.n : ",rsakey.key.n)
print("rsakey.key.p : ",rsakey.key.p)
print("rsakey.key.q : ",rsakey.key.q)
print("rsakey.key.u : ",rsakey.key.u)
"""