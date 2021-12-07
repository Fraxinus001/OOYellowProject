import AES256_synth
from IDCSys_Database import IDCSys_Database
import datetime


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.DateTimeNow = None
        self.counter = 0
        # self.readmode_all()

    @staticmethod
    def q_name():
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        a = LN + ", " + FN + ", " + MN
        return a

    @staticmethod
    def q_addr():
        HN = input("Please input the registrant's House No. / Street / Village, Subd.: ")
        BA = input("Please input the registrant's Barangay: ")
        CT = input("Please input the registrant's City / Municipality: ")
        PR = input("Please input the registrant's Province: ")
        ZC = input("Please input the registrant's Zip Code: ")
        b = HN + ", " + BA + ", " + CT + ", " + PR + " | ZIP:" + ZC
        return b

    @staticmethod
    def q_contno():
        c = "+63" + input("Please input the registrant's Contact Number (+63): ")
        return c

    @staticmethod
    def q_bday():
        d = input("Please input the registrant's Birthday: ")
        return d

    @staticmethod
    def q_natl():
        e = input("Please input the registrant's Nationality: ")
        return e

    @staticmethod
    def q_occp():
        f = input("Please input the registrant's Latest Occupation: ")
        return f
        
    def menu(self):
        print("\033[95mAdd new person\033[0m\n"
              "Prior to adding the person's record in the database, please\n"
              "prepare the following details:\n"
              "Valid ID(s), Birth Certificate, Occupation, Licenses(such as:\n"
              "Driver's, Engineering, Teaching License, if ever exist(s),\n"
              "and Benefits(GSIS, SSS, TIN, etc. if ever exist(s).")
        input("Please press any key to continue.")
        ask = input("DEMO: Confimation: ")
        if ask == "DEMO":
            print("Demonstration Mode.")
        UUID = input("Generate UUID? (yes, no): ") or self.UUID_DEMO
        if UUID == self.UUID_DEMO or UUID == "no":
            UUID = self.UUID_DEMO
            print(f"DEMO: UUID {self.UUID_DEMO} loaded!")
        elif UUID == "yes":
            self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
            UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
            self.d1.add(UUID, [])
            print("The UUID has been generated. Please take note of this for the Registrant.")
            print(f"{UUID}")
        ask = input("DEMO: Confimation: ")
        if ask == "DEMO":
            a = self.KeyEncrypt("Tale, Francis, Sales")
            b = self.KeyEncrypt("Blk. 8 Lt. 36 Ph. 3 Isabel Terraces Metro Manila Hills, San Jose, Rodriguez, Rizal | ZIP:1860")
            c = self.KeyEncrypt("+639569046959")
            d = self.KeyEncrypt("10-29-2001")
            e = self.KeyEncrypt("Filipino")
            f = self.KeyEncrypt("Engineer")
            g = self.KeyEncrypt("")
        else:
            print("\033[95mName:\033[0m")
            a = self.KeyEncrypt(self.q_name())
            print("\033[95mAddress:\033[0m")
            b = self.KeyEncrypt(self.q_addr())
            print("\033[95mOther Details:\033[0m")
            c = self.KeyEncrypt(self.q_contno())
            d = self.KeyEncrypt(self.q_bday())
            e = self.KeyEncrypt(self.q_natl())
            f = self.KeyEncrypt(self.q_occp())
            g = self.KeyEncrypt(input(""))
        specified = [a, b, c, d, e, f, g]
        for i in specified:
            self.w_addrecord(self.d1, UUID, self.counter, i)
            self.counter += 1
        self.counter = 0
        print("///  END OF QUERY  ///")
        print(f"\033[95mUUID: \033[0m{UUID}")
        print(f"\033[95mName: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][0])}")
        print(f"\033[95mAddress: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][1])}")
        print(f"\033[95mContact No.: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][2])}")
        print(f"\033[95mBirthday: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][3])}")
        print(f"\033[95mNationality: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][4])}")
        print(f"\033[95mOccupation: \033[0m{self.KeyDecrypt_utf(self.d1[UUID][5])}")
        print(f"\033[95mRESERVED\033[0m{self.KeyDecrypt_utf(self.d1[UUID][6])}")
        for i in specified:
            if self.d1[UUID][self.counter] == i:
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
        print("\033[95mThe above data were all accounted for and successfully "
              "recorded in the database.\033[0m")
        input("\033[95mPlease press any key to continue.\033[0m")
        # self.writemode_all()
            