# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt
import pickle
import base64

class AES256_synth:
    def __init__(self, AccessKey):
        self.password = "12345"
        self.AccessKey = AccessKey
        
    def pvkread(self, data):
        return open(data, "rb")
    
    def load_pvk(self, cls):
        self.loadsalt = self.pvkread("IDCSys_0x001.pvk")
        if cls == KeyEncrypt(AES256_synth).__class__:
            self.salt = base64.b64decode(pickle.load(self.loadsalt))
            AES256_encrypt.get_private_key(self.password, self.salt)
        elif cls == KeyDecrypt(AES256_synth).__class__:
            self.salt = base64.b64decode(pickle.load(self.loadsalt))
            AES256_decrypt.get_private_key(self.password, self.salt)
        self.loadsalt.close()
            
        
class KeyEncrypt(AES256_synth):
    def KeyEncrypt(self):
        self.load_pvk(self.__class__)
        Enc = AES256_encrypt.KeyEncrypt(self.AccessKey, self.password, self.salt)
        return Enc

class KeyDecrypt(AES256_synth):
    def KeyDecrypt(self, code):
        self.load_pvk(self.__class__)
        KeyDecrypt = AES256_decrypt.KeyDecrypt(code, self.password, self.salt)
        return KeyDecrypt
    