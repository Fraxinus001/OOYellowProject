# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt
import pickle
import base64
from cryptography.fernet import Fernet as fernet

class AES256_synth:
    def __init__(self, AccessKey):
        self.password = "12345"
        self.AccessKey = AccessKey
        self.salt = 0
        
    def pvkread(self, data):
        return open(data, "rb")
    
    def load_pvk(self, cls):
        loadsalt = self.pvkread("IDCSys_0x001.pvk")
        if cls == KeyEncrypt(AES256_synth).__class__:
            self.salt = base64.b64decode(pickle.load(loadsalt))
            AES256_encrypt.get_private_key(self.password, self.salt)
        elif cls == KeyDecrypt(AES256_synth).__class__:
            self.salt = base64.b64decode(pickle.load(loadsalt))
            AES256_decrypt.get_private_key(self.password, self.salt)
        elif cls == FernetKey(AES256_synth).__class__:
            key = b'Tfc7W_L8_8FSTVpmS0LSZgdzCYLh8tXIqpyS5n3dQPU='
            return key
        loadsalt.close()
            
        
class KeyEncrypt(AES256_synth):
    def KeyEncrypt(self):
        self.load_pvk(self.__class__)
        Enc = AES256_encrypt.KeyEncrypt(self.AccessKey, self.password, self.salt)
        self.salt = 0
        return Enc


class KeyDecrypt(AES256_synth):
    def KeyDecrypt(self, code):
        self.load_pvk(self.__class__)
        Dec = AES256_decrypt.KeyDecrypt(code, self.password, self.salt)
        self.salt = 0
        return Dec
    
    
class FernetKey(AES256_synth):
    def FernetKey(self):
        key = self.load_pvk(self.__class__)
        return key
    

#print(f"debug: {FernetKey(AES256_synth).FernetKey()}")
#a = KeyEncrypt("apple").KeyEncrypt()
#print(a)
#print(KeyDecrypt(AES256_synth).KeyDecrypt(a).decode('utf-8'))