from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

bestand = open("public.pem", "rb")
public_key = RSA.import_key(bestand.read())
bestand.close()

bestand = open("message.txt", "rb")
message = bestand.read()
bestand.close()

bestand = open("signature.bin", "rb")
signature = bestand.read()
bestand.close()

h = SHA256.new(message)

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature OK")
except:
    print("Signature NOT OK!!!")