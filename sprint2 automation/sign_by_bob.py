from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

bestand = open("private.pem", "wb")
bestand.write(private_key)
bestand.close()

bestand = open("public.pem", "wb")
bestand.write(public_key)
bestand.close()

bestand = open("message.txt", "rb")
message = bestand.read()
bestand.close()

h = SHA256.new(message)

signature = pkcs1_15.new(key).sign(h)

bestand = open("signature.bin", "wb")
bestand.write(signature)
bestand.close()

print("Bericht is ondertekend")