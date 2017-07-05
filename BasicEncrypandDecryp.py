import include.key as key
import include.msg as msg

bits = 128
message = '1234'
print("msg :",message)

key.saveKey(key.createKeyPair(bits))
rsakey = key.importKey('PublicKey.pem')
keySize = rsakey.size()
messageSize = len(message)
message = message.encode()

if (msg.checkSize(rsakey, messageSize)):
    ciphertext = rsakey.encrypt(message, 0)[-1]
else:
    keySize +=1
    keySize /=8
    keySize =int(keySize)
    ciphertext =b''
    message = [message[i:i+keySize] for i in range(0, len(message), keySize)]
    for mess in message :
        ciphertext+=rsakey.encrypt(mess,0)[-1]
        
with open('cipher','wb') as text_file:
    text_file.write(ciphertext)
print(ciphertext.decode("utf-8","ignore"))

rsakey = key.importKey('PrivateKey.pem')
keySize = rsakey.size()
with open('cipher','rb') as text_file:
    ciphertext = text_file.read()
cipherSize = len(ciphertext)
if (msg.checkSize(rsakey, cipherSize)):
    text = rsakey.decrypt(ciphertext)
    print(text.decode('utf-8', 'ignore'))
else:
    keySize +=1
    keySize /=8
    keySize =int(keySize)
    text =b''
    ciphertext = [ciphertext[i:i+keySize] for i in range(0, len(ciphertext), keySize)]
    for ctext in  ciphertext :
        text += rsakey.decrypt(ctext)
    print(text.decode('utf-8', 'ignore'))
"""
print("Key Size :",keySize)
print("Cipher Size :",cipherSize)
print("rsakey.key.e : ",rsakey.key.e)
print("rsakey.key.d : ",rsakey.key.d)
print("rsakey.key.n : ",rsakey.key.n)
print("rsakey.key.p : ",rsakey.key.p)
print("rsakey.key.q : ",rsakey.key.q)
print("rsakey.key.u : ",rsakey.key.u)

"""