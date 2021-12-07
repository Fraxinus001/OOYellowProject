import AES256_synth
from IDCSys_Database import IDCSys_Database


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.UUID = ''
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None
        self.counter = 0
        self.goback = False
        self.menu_map = {
            "1": self.q_name,
            "2": self.q_addr,
            "3": self.q_contno,
            "4": self.q_bday,
            "5": self.q_natl,
            "6": self.q_occp,
            "7": self.d_finalize,
            "8": self.back,
        }

    def q_name(self):
        print("\033[95mName:\033[0m")
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        a = LN + ", " + FN + ", " + MN
        self.a = a

    def q_addr(self):
        print("\033[95mAddress:\033[0m")
        HN = input("Please input the registrant's House No. / Street / Village, Subd.: ")
        BA = input("Please input the registrant's Barangay: ")
        CT = input("Please input the registrant's City / Municipality: ")
        PR = input("Please input the registrant's Province: ")
        ZC = input("Please input the registrant's Zip Code: ")
        b = HN + ", " + BA + ", " + CT + ", " + PR + " | ZIP:" + ZC
        self.b = b

    def q_contno(self):
        c = "+63" + input("Please input the registrant's Contact Number (+63): ")
        self.c = c

    def q_bday(self):
        d = input("Please input the registrant's Birthday: ")
        self.d = d

    def q_natl(self):
        e = input("Please input the registrant's Nationality: ")
        self.e = e

    def q_occp(self):
        f = input("Please input the registrant's Latest Occupation: ")
        self.f = f
    
    def d_finalize(self):
        print("///  END OF QUERY  ///")
        print(f"\033[95mUUID: \033[0m{self.UUID}")
        print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][0])}")
        print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][1])}")
        print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][2])}")
        print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][3])}")
        print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][4])}")
        print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][5])}")
        print(f"\033[95mRESERVED\033[0m{self.KeyDecrypt_utf(self.d1[self.UUID][6])}")
    
    def back(self):
        self.goback = True
    
    def menu(self):
        print("\033[95mChange existing Record\033[0m\n"
              "You are hereby will be authorized for changing any data by the\n"
              "security manager for clearance.")
        input("\033[95mPlease press any key to continue.\033[0m\n")
        print("Demonstration Mode.")
        print("\033[95mAuthorization:\033[0m")

        self.UUID = input("Please input the existing registrant's UUID: ") or self.UUID_DEMO
        if self.UUID == self.UUID_DEMO:
            print(f"DEMO: UUID {self.UUID_DEMO} loaded!")
            print("Demonstration Mode.")
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
        if self.a is None:
            self.a = self.KeyDecrypt_utf(self.d1[self.UUID][0])
        elif self.b is None:
            self.b = self.KeyDecrypt_utf(self.d1[self.UUID][1])
        elif self.c is None:
            self.c = self.KeyDecrypt_utf(self.d1[self.UUID][2])
        elif self.d is None:
            self.d = self.KeyDecrypt_utf(self.d1[self.UUID][3])
        elif self.e is None:
            self.e = self.KeyDecrypt_utf(self.d1[self.UUID][4])
        elif self.f is None:
            self.f = self.KeyDecrypt_utf(self.d1[self.UUID][5])
        elif self.g is None:
            self.g = self.KeyDecrypt_utf(self.d1[self.UUID][6])
        specified = [self.a, self.b, self.c, self.d, self.e, self.f, self.g]
        for i in specified:
            self.w_addrecord(self.d1, self.UUID, self.counter, i)
            self.counter += 1
        self.counter = 0

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
                elif self.counter == 6:
                    print("RESERVED confirmed.")
                self.counter += 1
        self.counter = 0
        self.f_dump_dx(self.d1)
        print("\033[95mThe above data were successfully recorded in the database.\033[0m")
        input("\033[95mPlease press any key to continue.\033[0m")
        