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
        self.password = None
        self.goback = False
        self.menu_map = {
            "1": self.q_name,
            "2": self.q_username(),
            "3": self.q_password(),
            "4": self.d_finalize,
            "5": self.back,
        }
    
    @staticmethod
    def q_username():
        username = input("Please input the user's Username: ")
        return username

    @staticmethod
    def q_password():
        password = None
        switch = 0
        while switch == 0:
            password = input("Please input the user's Password: ")
            if len(password) < 6:
                print("Password too short. Must not be less than 6 characters.")
            else:
                switch = 1
        return password

    @staticmethod
    def q_name():
        FN = input("Please input the user's First Name: ")
        MN = input("Please input the user's Middle Name: ")
        LN = input("Please input the user's Last Name: ")
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
                    if username not in self.dA2[b'Read']:
                        self.dA2[i].insert(-1, username)
                    else:
                        pass
        else:
            pass
        if W == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Write':
                    if username not in self.dA2[b'Write']:
                    self.dA2[i].insert(-1, username)
        else:
            pass
        if M == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Modify':
                    self.dA2[i].insert(-1, username)
        else:
            pass
        if D == "yes":
            for i in self.dA2:
                if self.KeyDecrypt_byt(i) == b'Delete':
                    self.dA2[i].insert(-1, username)
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

    def d_finalize(self):
        print("///  END OF QUERY  ///")
        if self.name is None or self.name == '':
            self.name = self.dA3[self.username]
        if self.username is None or self.username == '':
            for i in self.dA3:
                if self.KeyDecrypt_utf(self.dA3[i]) == self.name:
                    self.username = i
        if self.password is None or self.password == '':
            self.password = self.dA1[self.username]
        if self.bday is None or self.bday == '':
            self.bday = self.d1[self.UUID][3]
        if self.natl is None or self.natl == '':
            self.natl = self.d1[self.UUID][4]
        if self.occp is None or self.occp == '':
            self.occp = self.d1[self.UUID][5]
        specified = [self.name, self.addr, self.contno, self.bday, self.natl, self.occp]
        for i in specified:
            self.w_addrecord(self.d1, self.UUID, i, self.counter)
            self.counter += 1
        self.counter = 0
        print(f"\033[95mUUID: \033[0m{self.UUID}")
        print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][0])}")
        print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][1])}")
        print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][2])}")
        print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][3])}")
        print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][4])}")
        print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][5])}")
        for i in specified:
            if self.d1[self.UUID][self.counter] == i:
                if self.counter == 0:
                    print("Name confirmed.")
                elif self.counter == 1:
                    print("Address confirmed.")
                elif self.counter == 2:
                    print("Contact No. confirmed.")
                elif self.counter == 3:
                    print("Birthday confirmed.")
                elif self.counter == 4:
                    print("Nationality confirmed.")
                elif self.counter == 5:
                    print("Occupation confirmed.")
                self.counter += 1
        self.counter = 0
        self.f_dump_d1(self.d1)
        self.f_dump_d2(self.d2)
        self.f_dump_d3(self.d3)
        self.f_dump_d4(self.d4)
        print("\033[95mThe above data were successfully recorded in the database.\033[0m")
        input("\033[95mPlease press any key to continue.\033[0m")
        pass

    def back(self):
        self.goback = True
    
    def menu(self):
        print("\033[95mAdministration: Delete user account\033[0m")
        print("Please login again to continue.")
        IDCSys_Core.IDCSys_Core().logged_in = False
        IDCSys_Core.IDCSys_Core().login()
        input("Please press any key to continue.")
        print("\033[95mAuthorization:\033[0m")
        a = self.KeyEncrypt(self.q_username())
        self.username = a
        ans = None
        try:
            for i in self.dA1:
                if i == a:
                    while True:
                        if self.goback is True:
                            break
                        print(f"""
                    \t\033[95m1 \t\033[0mChange Name
                    \t\033[95m2 \t\033[0mChange Address
                    \t\033[95m3 \t\033[0mChange Contact No.
                    \t\033[95m4 \t\033[0mChange Birthday
                    \t\033[95m5 \t\033[0mNationality
                    \t\033[95m6\t\033[0mOccupation
                    \t\033[95m7\t\033[0mFinalize
                    \t\033[95m8\t\033[0mGo Back
                                                  """)
                        answer = input("Please enter a command: ").lower()
                        try:
                            func = self.menu_map[answer]
                        except KeyError:
                            print("{} is not a valid option".format(answer))
                        else:
                            func()
