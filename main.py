from OpenSSL import crypto

bits = 32


def createKeyPair(bits):
    """Create Key Pair"""
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, bits)
    return pkey


def saveKey(pkey):
    """Save Key Pair to file"""
    prkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey)
    with open("PrivateKey.pem", "w",encoding='UTF-8') as text_file:
        print(prkey.decode("UTF-8"), file=text_file)
    pukey = crypto.dump_publickey(crypto.FILETYPE_PEM, pkey)
    with open("PublicKey.pem", "w",encoding='UTF-8') as text_file:
        print(pukey.decode("UTF-8"), file=text_file)
    print("Complete Save key")
    return True

#k = saveKey(createKeyPair(bits))
#print(Encrypt('Test', 'PublicKey.pem', 'Public'))
