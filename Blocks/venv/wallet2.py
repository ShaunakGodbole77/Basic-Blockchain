from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

def generatekeys():
    private_key = RSA.generate(2048)
    public_key = private_key.public_key()
    priv_string = str(private_key)
    pub_string = str(public_key)
    priv = open("privateKey.txt","w")
    priv.write(priv_string)
    priv.close()
    pubk = open("publicKey.txt","w")
    pubk.write(pub_string)
    pubk.close()
    print(private_key)
    print(public_key)

def encryption_data(mydata,private_key,publickey):
    key = Fernet.generate_key()
    print(key)
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(bytes(mydata,"UTF-8"))
    print(encrypted_data)
    encrypt_key = rsa.encrypt(key,private_key)
    encrypted_key = rsa.encrypt(encrypt_key,publickey)
    print(encrypted_key)

def decryption_data(mydata,private_key,encrypted_key,public_key):
    dpubkey = rsa.decrypt(encrypted_key,private_key)
    decrypt_key = rsa.decrypt(dpubkey,public_key)
    cipher = Fernet(decrypt_key)
    decrypted_data = cipher.decrypt(edata)
    print(decrypted_data.decode())

generatekeys()