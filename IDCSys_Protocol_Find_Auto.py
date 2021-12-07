from IDCSys_Database import IDCSys_Database


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.UUID = ''

    def menu(self):
        print("\033[95mFind records (automated)\033[0m\n"
              "You are hereby will be authorized to view existing records")
        input("\033[95mPlease press any key to continue.\033[0m\n")
        print("Demonstration Mode.")
        print("\033[95mAuthorization:\033[0m")
        self.UUID = input("Please input the existing registrant's UUID: ") or self.UUID_DEMO
        if self.UUID == self.UUID_DEMO:
            print(f"\033[95mUUID: \033[0m{self.UUID}")
            print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][0])}")
            print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][1])}")
            print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][2])}")
            print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][3])}")
            print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][4])}")
            print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][5])}")

            print(f"\033[95m[Beneficiaries] \033[0m")
            print(f"\033[95mSSS: \033[0m{self.KeyDecrypt_utf(self.d2[self.UUID][0])}")
            print(f"\033[95mGSIS: \033[0m{self.KeyDecrypt_utf(self.d2[self.UUID][1])}")

            print(f"\033[95m[Credentials] \033[0m")
            print(f"\033[95mValid ID.: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][0])}")
            print(f"\033[95mBarangay ID: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][1])}")
            print(f"\033[95mNBI: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][2])}")
            print(f"\033[95mPassport: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][3])}")
            print(f"\033[95mDriver's:\033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][4])}")

            print(f"\033[95m[TAX Data] \033[0m")
            print(f"\033[95mTIN: \033[0m{self.KeyDecrypt_utf(self.d4[self.UUID][0])}")
            print(f"\033[95mCedula: \033[0m{self.KeyDecrypt_utf(self.d4[self.UUID][1])}")
        else:
            print(f"\033[95mUUID: \033[0m")
            print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][0])}")
            print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][1])}")
            print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][2])}")
            print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][3])}")
            print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][4])}")
            print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][5])}")
            
            print(f"\033[95m[Beneficiaries] \033[0m{self.UUID}")
            print(f"\033[95mSSS: \033[0m{self.KeyDecrypt_utf(self.d2[self.UUID][0])}")
            print(f"\033[95mGSIS: \033[0m{self.KeyDecrypt_utf(self.d2[self.UUID][1])}")
            
            print(f"\033[95m[Credentials] \033[0m")
            print(f"\033[95mValid ID.: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][0])}")
            print(f"\033[95mBarangay ID: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][1])}")
            print(f"\033[95mNBI: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][2])}")
            print(f"\033[95mPassport: \033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][3])}")
            print(f"\033[95mDriver's:\033[0m{self.KeyDecrypt_utf(self.d3[self.UUID][4])}")
            
            print(f"\033[95m[TAX Data] \033[0m")
            print(f"\033[95mTIN: \033[0m{self.KeyDecrypt_utf(self.d4[self.UUID][0])}")
            print(f"\033[95mCedula: \033[0m{self.KeyDecrypt_utf(self.d4[self.UUID][1])}")
        input("\033[95mPlease press any key to continue.\033[0m\n")
        