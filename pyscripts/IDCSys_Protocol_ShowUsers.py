import IDCSys_Core
from IDCSys_Database import IDCSys_Database


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.dat0A1 = self.readmode("dat0A1.db")
        self.dat0A2 = self.readmode("dat0A2.db")
        self.dat0A3 = self.readmode("dat0A3.db")
        self.dA1 = self.f_load(self.dat0A1)
        self.dA2 = self.f_load(self.dat0A2)
        self.dA3 = self.f_load(self.dat0A3)
        self.name = None
        self.username = None
    
    @staticmethod
    def q_username():
        username = input("Please input the registrant's Username: ")
        return username
    
    def menu(self):
        print("\033[95mAdministration: Display user account\033[0m")
        print("Please login again to continue.")
        IDCSys_Core.IDCSys_Core().logged_in = False
        IDCSys_Core.IDCSys_Core().login()
        input("Please press any key to continue.")
        FN = []
        usn = []
        writeperms = []
        modifyperms = []
        deleteperms = []
        readperms = []
        for i in self.dA1:
            usn.append(self.KeyDecrypt_utf(i))
        for i in self.dA2:
            if self.KeyDecrypt_utf(i) == 'Write':
                for j in self.dA2[i]:
                    writeperms.append(self.KeyDecrypt_utf(j))
        for i in self.dA2:
            if self.KeyDecrypt_utf(i) == 'Modify':
                for j in self.dA2[i]:
                    modifyperms.append(self.KeyDecrypt_utf(j))
        for i in self.dA2:
            if self.KeyDecrypt_utf(i) == 'Delete':
                for j in self.dA2[i]:
                    deleteperms.append(self.KeyDecrypt_utf(j))
        for i in self.dA2:
            if self.KeyDecrypt_utf(i) == 'Read':
                for j in self.dA2[i]:
                    readperms.append(self.KeyDecrypt_utf(j))
        for i in self.dA3:
            FN.append(self.KeyDecrypt_utf(self.dA3[i]))
        
        print(f"\t\033[95mFull Names: \t\033[0m{FN}")
        print(f"\t\033[95mUsernames: \t\033[0m{usn}")
        print(f"\t\033[95mWrite Permissions: \t\033[0m{writeperms}")
        print(f"\t\033[95mModify Permissions: \t\033[0m{modifyperms}")
        print(f"\t\033[95mDelete Permissions: \t\033[0m{deleteperms}")
        print(f"\t\033[95mRead Permissions: \t\033[0m{readperms}")
