# ID Centralization System

import AES256_synth


class IDCSys_Core:
    def __init__(self):
        self.UUID = "IDCSys-<TestPass02>-sySCDI"
        self.AES_1 = AES256_synth.KeyEncrypt
        self.AES_2 = AES256_synth.KeyDecrypt
        
    def IDCSys_Encrypt(self):
        EncryptDat = self.AES_1(self.UUID).KeyEncrypt()
        print(f"debug: {EncryptDat}")
        return EncryptDat
        
    def IDCSys_Decrypt(self):
        print(f"debug: {self.AES_2('').KeyDecrypt(self.AES_1(self.UUID).KeyEncrypt())}")
        
    def mainmenu(self):
        print("Welcome to ID Centralization System")
        if self.UUID != '':
            print(f"debug: Running!")
        else:
            print(f"debug: failing..")


if __name__ == '__main__':
    IDCSys_Core().IDCSys_Encrypt()
    IDCSys_Core().IDCSys_Decrypt()
    IDCSys_Core().mainmenu()
