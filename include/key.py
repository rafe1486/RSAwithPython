from OpenSSL import crypto
from Crypto.PublicKey import RSA

def createKeyPair(bits):
    """Create Key Pair by using OpenSSL"""
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, bits)
    return pkey

def saveKey(pkey):
    """Save Key Pair to file"""
    prkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey)
    with open("key/PrivateKey.pem", "w",encoding='UTF-8') as text_file:
        print(prkey.decode("UTF-8"), file=text_file)
    pukey = crypto.dump_publickey(crypto.FILETYPE_PEM, pkey)
    with open("key/PublicKey.pem", "w",encoding='UTF-8') as text_file:
        print(pukey.decode("UTF-8"), file=text_file)
    print("Complete Save key")
    return True

def getKeySize(key):
    """return keysize"""
    return key.size()+1

def getKeyLength(key):
    """return keylength per charecter"""
    return int((key.size()+1)/8)

def getHalfofKeyLength(key):
    """return int of keylength devide by 2 """
    return int(getKeyLength(key)/2)

def importKey(fileName):
    with open("key/"+fileName, 'rb') as file:
        keydata = file.read()
        rsakey = RSA.importKey(keydata)
        file.close()
    return rsakey