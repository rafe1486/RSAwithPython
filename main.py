from OpenSSL import crypto

Type = crypto.TYPE_RSA
bits = 32


def createKeyPair(type, bits):
    """Create Key Pair"""
    pkey = crypto.PKey()
    pkey.generate_key(type, bits)
    return pkey


def saveKey(pkey):
    """Save Key Pair to text file"""
    prkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey)
    with open("PrivateKey.pem", "w",encoding='UTF-8') as text_file:
        print(prkey.decode("UTF-8"), file=text_file)
    pukey = crypto.dump_publickey(crypto.FILETYPE_PEM, pkey)
    with open("PublicKey.pem", "w",encoding='UTF-8') as text_file:
        print(pukey.decode("UTF-8"), file=text_file)
    return 0


def Encrypt(text, keyFileName, type):
    """Encode Text"""
    if type == 'Public':
        with open(keyFileName, "r",) as input:
          publicKey = crypto.load_publickey(crypto.FILETYPE_PEM, input.read())
          return  crypto.sign(publicKey,"Test Encode by Public Key","sha1")
    if type == 'Private':
        with open(keyFileName, "r",) as input:
          privateKey = crypto.load_privatekey(crypto.FILETYPE_PEM, input.read())
          return  crypto.sign(publicKey,"Test Encode by Private Key","sha1")

def Decrypt(signature, keyFileName, type):
    """Decode Text"""
    if type == 'Public':
        with open(keyFileName, "r",) as input:
          publicKey = crypto.load_publickey(crypto.FILETYPE_PEM, input.read())
          #return crypto.verify
    if type == 'Private':
        with open(keyFileName, "r",) as input:
          privateKey = crypto.load_privatekey(crypto.FILETYPE_PEM, input.read())




k = saveKey(createKeyPair(Type, bits))
print(Encrypt('Test', 'PublicKey.pem', 'Public'))
