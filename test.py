from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

message = b'asdfc'

with open('Publickey.pem','rb') as privatefile:
    keydata = privatefile.read()
    publickey = serialization.load_pem_private_key(
        privatefile.read(),
        password=None,
        backend=default_backend()
    )