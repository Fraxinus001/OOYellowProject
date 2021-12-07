from IDCSys_Database import IDCSys_Database


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.name = ''
    
    def menu(self):
        print("\033[95mFind records (automated)\033[0m\n"
              "You are hereby will be authorized to view existing records")
        input("\033[95mPlease press any key to continue.\033[0m\n")
        print("Demonstration Mode.")
        print("\033[95mAuthorization:\033[0m")
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        self.name = LN + ", " + FN + ", " + MN
        for i in self.d1:
            if self.KeyDecrypt_utf(self.d1[i][0]) == self.name:
                print(f"\033[95mUUID: \033[0m{i}")
                print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[i][0])}")
                print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[i][1])}")
                print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[i][2])}")
                print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[i][3])}")
                print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[i][4])}")
                print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[i][5])}")
                print(f"\033[95mRESERVED\033[0m{self.KeyDecrypt_utf(self.d1[i][6])}")
        input("\033[95mPlease press any key to continue.\033[0m\n")
