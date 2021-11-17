#ID Centralization System

import AES256_synth

class IDCSys_Core():
    def __init__(self):
        self.UUID = "TestPass02"
        self.AES_1 = AES256_synth.AES256_synth
        
    def IDCSYS_Encrypt(self):
        EncryptDat = self.AES_1(self.UUID).KeyEncrypt()
        print(EncryptDat)
        return EncryptDat
        
    def IDCSYS_Decrypt(self):
        print(self.AES_1("").KeyDecrypt(self.AES_1(self.UUID).KeyEncrypt()))
        
    def mainmenu(self):
        print("Welcome to ID Centralization System")


IDCSys_Core().IDCSYS_Encrypt()
IDCSys_Core().IDCSYS_Decrypt()