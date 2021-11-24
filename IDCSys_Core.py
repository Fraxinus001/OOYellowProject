# ID Centralization System

import AES256_synth
import IDCSys_Database
import IDCSys_Authorizor

# Set up a test user and permission
# Permits to operate
IDCSys_Authorizor.authorizor.add_permission("test program")
IDCSys_Authorizor.authorizor.add_permission("change program")
# Dominic Edward G. Ty
IDCSys_Authorizor.authenticator.add_user("degty@idcsys.com", "12345")
IDCSys_Authorizor.authorizor.permit_user("test program", "degty@idcsys.com")
IDCSys_Authorizor.authorizor.permit_user("change program", "degty@idcsys.com")
# Francis S. Tale
IDCSys_Authorizor.authenticator.add_user("fstale@idcsys.com", "12345")
IDCSys_Authorizor.authorizor.permit_user("test program", "fstale@idcsys.com")
IDCSys_Authorizor.authorizor.permit_user("change program", "fstale@idcsys.com")


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
