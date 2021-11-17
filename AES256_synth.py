# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt


class AES256_synth:
    def __init__(self, AccessKey):
        self.password = "12345"
        self.AccessKey = AccessKey
    
    def KeyEncrypt(self):
        Enc = AES256_encrypt.KeyEncrypt(self.AccessKey, self.password)
        return Enc
    
    def KeyDecrypt(self, code):
        KeyDecrypt = AES256_decrypt.KeyDecrypt(code, self.password)
        return KeyDecrypt
