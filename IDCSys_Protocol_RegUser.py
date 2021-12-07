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
        
    @staticmethod
    def q_username():
        username = input("Please input the registrant's Username: ")
        return username
    
    @staticmethod
    def q_password():
        password = input("Please input the registrant's Password: ")
        return password

    @staticmethod
    def q_name():
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        a = LN + ", " + FN + ", " + MN
        return a

    def q_perms(self, username):
        R = input("Allow Read? (yes or no): ")
        W = input("Allow Write? (yes or no): ")
        M = input("Allow Modify? (yes or no): ")
        D = input("Allow Delete? (yes or no): ")
        if R == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Read':
                    self.dA2[i].add(username)
                    self.dA2[i].update()
        else:
            pass
        if W == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Write':
                    self.dA2[i].add(username)
                    self.dA2[i].update()
        else:
            pass
        if M == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Modify':
                    self.dA2[i].add(username)
                    self.dA2[i].update()
        else:
            pass
        if D == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Delete':
                    self.dA2[i].add(username)
                    self.dA2[i].update()
        else:
            pass
        
    def d_perms(self, username):
        perms_list = []
        for i in self.dA2:
            if self.KeyDecrypt_byt(i) == b'Read':
                for j in self.dA2[i]:
                    if j == username:
                        perms_list.append(b'Read')
        for i in self.dA2:
            if self.KeyDecrypt_byt(i) == b'Write':
                for j in self.dA2[i]:
                    if j == username:
                        perms_list.append(b'Write')
        for i in self.dA2:
            if self.KeyDecrypt_byt(i) == b'Modify':
                for j in self.dA2[i]:
                    if j == username:
                        perms_list.append(b'Modify')
        for i in self.dA2:
            if self.KeyDecrypt_byt(i) == b'Delete':
                for j in self.dA2[i]:
                    if j == username:
                        perms_list.append(b'Delete')
        return perms_list
        
    def menu(self):
        print("\033[95mAdministration: Register new user account\033[0m")
        print("Please login again to continue.")
        IDCSys_Core.IDCSys_Core().logged_in = False
        IDCSys_Core.IDCSys_Core().login()
        input("Please press any key to continue.")
        a = self.KeyEncrypt(self.q_username())
        b = self.KeyEncrypt(self.q_password())
        c = self.KeyEncrypt(self.q_name())
        self.q_perms(a)
        self.w_addreg(self.dA1, a, b)
        self.w_addreg(self.dA3, a, c)
        print("///  END OF QUERY  ///")
        print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.dA3[a])}")
        print(f"\033[95mUsername: \033[0m{self.KeyDecrypt_utf(a)}")
        print(f"\033[95mPassword: \033[0m{self.KeyDecrypt_utf(self.dA1[a])}")
        print(f"\033[95mPermission(s): \033[0m{self.d_perms(a)}")
        x = self.writemode("dat0A1.db")
        self.w_dump(self.dA1, x)
        self.f_close(x)
        x = self.writemode("dat0A2.db")
        self.w_dump(self.dA2, x)
        self.f_close(x)
        x = self.writemode("dat0A3.db")
        self.w_dump(self.dA3, x)
        self.f_close(x)
        print("\033[95mThe above data were all accounted for and successfully "
              "recorded in the database.\033[0m")
        ans = input("\033[95mRestart the program to apply changes? (yes or no) \033[0m")
        if ans == "yes":
            raise SystemExit()
        else:
            pass
        input("\033[95mPlease press any key to continue.\033[0m")

        