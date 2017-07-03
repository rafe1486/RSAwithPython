import include.key as key

def checkSize(rsakey, messageSize):
    """
    compare key size with msg
    if KeySize >= msgSize return True
    if KeySize < msgSize return False
    """
    keySize = key.getKeyLength(rsakey)
    if(keySize >= messageSize):
        return True
    if(keySize < messageSize):
        return False

def getLength(msg):
    """
    return length of msg
    """
    return len(msg)

def msgtoDec(msg):
    """
    return Decimal of msg
    """
    if(isinstance(msg, str)):
        return int.from_bytes(msg.encode(),byteorder="little")
    else:
        return int.from_bytes(msg,byteorder="little")

def dectoMsg(dec,rsakey):
    if(isinstance(dec, int)):
        return dec.to_bytes(key.getHalfofKeyLength(rsakey), byteorder="little").decode('utf-8', 'ignore')
    else:
        dec = int(dec)
        return dec.to_bytes(key.getHalfofKeyLength(rsakey), byteorder="little").decode('utf-8', 'ignore')