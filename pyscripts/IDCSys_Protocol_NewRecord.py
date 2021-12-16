import AES256_synth
from IDCSys_Database import IDCSys_Database
import datetime


class Protocol(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.DateTimeNow = None
        self.counter = 0
        # self.readmode_all()

    # Function calls for queries.
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
    
    @staticmethod
    def q_beneficiaries_sss():
        ans = input("Do the registrant have Social Security System? (yes or no) ")
        if ans == "yes":
            g = input("Please input the registrant's Social Security Number (SSS): ")
            return g
        else:
            return "Not Available"
    
    @staticmethod
    def q_beneficiaries_gsis():
        ans = input("Do the registrant have a Government Service Insurance System? (yes or no) ")
        if ans == "yes":
            h = input("Please input the registrant's Government Service Insurance System Number (GSIS): ")
            return h
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_passport():
        ans = input("Do the registrant have a Passport? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's Passport no.: ")
            return i
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_drivid():
        ans = input("Do the registrant have a Driver's ID? (yes or no) ")
        if ans == "yes":
            j = input("Please input the registrant's Driver's ID no.: ")
            return j
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_profession():
        ans = input("Do the registrant have a Professional License? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's Professional License no.: ")
            return i
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_valID():
        ans = input("Do the registrant have a Valid ID? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's primary Valid ID no.: ")
            return i
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_nbi():
        ans = input("Do the registrant have NBI Clearance? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's NBI Clearance no.: ")
            return i
        else:
            return "Not Available"
    
    @staticmethod
    def q_credentials_barid():
        ans = input("Do the registrant have a Barangay ID? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's Baranday ID no.: ")
            return i
        else:
            return "Not Available"
        
    @staticmethod
    def q_taxdata_tindata():
        ans = input("Do the registrant have a Taxpayer's ID? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's Taxpayer's Identification No.: ")
            return i
        else:
            return "Not Available"
        
    @staticmethod
    def q_taxdata_cedula():
        ans = input("Do the registrant have a Cedula? (yes or no) ")
        if ans == "yes":
            i = input("Please input the registrant's Cedula no.: ")
            return i
        else:
            return "Not Available"
        
    # Main Menu for New Records
    def menu(self):
        print("\033[95mAdd new person\033[0m\n"
              "Prior to adding the person's record in the database, please\n"
              "prepare the following details:\n"
              "Valid ID(s), Birth Certificate, Occupation, Licenses(such as:\n"
              "Driver's, Engineering, Teaching License, if ever exist(s),\n"
              "and Benefits(GSIS, SSS, TIN, etc. if ever exist(s).")
        input("Please press any key to continue.")
        print("Demonstration Mode.")
        UUID = input("Generate UUID (For DEMO, enter no)? (yes, no): ") or self.UUID_DEMO
        if UUID == self.UUID_DEMO or UUID == "no":
            UUID = self.UUID_DEMO
            print(f"DEMO: UUID {self.UUID_DEMO} loaded!")
        elif UUID == "yes":
            self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
            UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
            print("The UUID has been generated. Please take note of this for the Registrant.")
            print(f"{UUID}")
        # For Demonstration: Ask for confirmation
        ask = input("DEMO: Confimation, input DEMO to continue: ")
        if ask == "DEMO":
            a = self.KeyEncrypt("Tale, Francis, Sales")
            b = self.KeyEncrypt("Blk. 8 Lt. 36 Ph. 3 Isabel Terraces Metro Manila Hills, San Jose, Rodriguez, Rizal | ZIP:1860")
            c = self.KeyEncrypt("+639569046959")
            d = self.KeyEncrypt("10-29-2001")
            e = self.KeyEncrypt("Filipino")
            f = self.KeyEncrypt("Student")
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
        specified = [a, b, c, d, e, f]
        for i in specified:
            self.w_addrecord(self.d1, UUID, i, self.counter)
            self.counter += 1
        self.counter = 0
        
        # For Beneficiaries:
        ans = (input("Skip Beneficiaries? (yes or no)"))
        if ans == "yes":
            a = self.KeyEncrypt("Not Available")
            b = self.KeyEncrypt("Not Available")
        else:
            a = self.KeyEncrypt(self.q_beneficiaries_sss())
            b = self.KeyEncrypt(self.q_beneficiaries_gsis())
        specified = [a, b]
        for i in specified:
            self.w_addrecord(self.d2, UUID, i, self.counter)
            self.counter += 1
        self.counter = 0
        
        # For Credentials:
        ans = (input("Skip Credentials? (yes or no)"))
        if ans == "yes":
            a = self.KeyEncrypt("Not Available")
            b = self.KeyEncrypt("Not Available")
            c = self.KeyEncrypt("Not Available")
            d = self.KeyEncrypt("Not Available")
            e = self.KeyEncrypt("Not Available")
            f = self.KeyEncrypt("Not Available")
        else:
            a = self.KeyEncrypt(self.q_credentials_valID())
            b = self.KeyEncrypt(self.q_credentials_barid())
            c = self.KeyEncrypt(self.q_credentials_nbi())
            d = self.KeyEncrypt(self.q_credentials_passport())
            e = self.KeyEncrypt(self.q_credentials_drivid())
            f = self.KeyEncrypt(self.q_credentials_profession())
        specified = [a, b, c, d, e, f]
        for i in specified:
            self.w_addrecord(self.d3, UUID, i, self.counter)
            self.counter += 1
        self.counter = 0
        
        # For TAXData:
        ans = (input("Skip TAX Data? (yes or no)"))
        if ans == "yes":
            a = self.KeyEncrypt("Not Available")
            b = self.KeyEncrypt("Not Available")
        else:
            a = self.KeyEncrypt(self.q_taxdata_tindata())
            b = self.KeyEncrypt(self.q_taxdata_cedula())
        specified = [a, b]
        for i in specified:
            self.w_addrecord(self.d4, UUID, i, self.counter)
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
        self.f_dump_d1(self.d1)
        self.f_dump_d2(self.d2)
        self.f_dump_d3(self.d3)
        self.f_dump_d4(self.d4)
        print("\033[95mThe above data were all accounted for and successfully "
              "recorded in the database.\033[0m")
        input("\033[95mPlease press any key to continue.\033[0m")
        # self.writemode_all()
            