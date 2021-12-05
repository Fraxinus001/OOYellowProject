import IDCSys_Database


class protocol(IDCSys_Database.IDCSys_Database):
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.counter = 0
        #self.readmode_all()
        
    def q_name(self):
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        a = LN + ", " + FN + ", " + MN
        return a
    
    def q_addr(self):
        HN = input("Please input the registrant's House No. / Street / Village, Subd.: ")
        BA = input("Please input the registrant's Barangay: ")
        CT = input("Please input the registrant's City / Municipality: ")
        PR = input("Please input the registrant's Province: ")
        ZC = input("Please input the registrant's Zip Code: ")
        b = HN + ", " + BA + ", " + CT + ", " + PR + " | ZIP:" + ZC
        return b
    
    def q_contno(self):
        c = "+63" + input("Please input the registrant's Contact Number (+63): ")
        return c
    
    def q_bday(self):
        d = input("Please input the registrant's Birthday: ")
        return d
    
    def q_natl(self):
        e = input("Please input the registrant's Nationality: ")
        return e
    
    def q_occp(self):
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
        print("Demonstration Mode.")
        UUID = input("Please input the registrant's UUID: ") or \
               b'PQVNe7ZhcwqnkW4cUI+/UfpSo4DO9gj52h4ah+gNbjrJzyrYr4sM41T5LBTR7t/5'
        if UUID == b'PQVNe7ZhcwqnkW4cUI+/UfpSo4DO9gj52h4ah+gNbjrJzyrYr4sM41T5LBTR7t/5':
            print("DEMO: UUID b'PQVNe7ZhcwqnkW4cUI+/UfpSo4DO9gj52h4ah+gNbjrJzyrYr4sM41T5LBTR7t/5' loaded!")
        ask = input("DEMO: Confimation: ")
        if ask == "DEMO":
            a = "Tale, Francis, Sales"
            b = "Blk. 8 Lt. 36 Ph. 3 Isabel Terraces Metro Manila Hills, San Jose, Rodriguez, Rizal| ZIP:1860"
            c = "+639569046959"
            d = "10-29-2001"
            e = "Filipino"
            f = "Engineer"
            g = ""
        else:
            print("\033[95mName:\033[0m")
            a = self.q_name()
            print("\033[95mAddress:\033[0m")
            b = self.q_addr()
            print("\033[95mOther Details:\033[0m")
            c = self.q_contno()
            d = self.q_bday()
            e = self.q_natl()
            f = self.q_occp()
            g = input("")
        specified = [a, b, c, d, e, f, g]
        for i in specified:
            self.w_addrecord(self.d1, UUID, self.counter, i)
            self.counter += 1
        self.counter = 0
        print("///  END OF QUERY  ///")
        print(f"\033[95mName: \033[0m{self.d1[UUID][0]}")
        print(f"\033[95mAddress: \033[0m{self.d1[UUID][1]}")
        print(f"\033[95mContact No.: \033[0m{self.d1[UUID][2]}")
        print(f"\033[95mBirthday: \033[0m{self.d1[UUID][3]}")
        print(f"\033[95mNationality: \033[0m{self.d1[UUID][4]}")
        print(f"\033[95mOccupation: \033[0m{self.d1[UUID][5]}")
        print(f"\033[95mRESERVED\033[0m{self.d1[UUID][6]}")
        input("\033[95mPlease press any key to continue.\033[0m")
        #self.writemode_all()
        self.f_dump_d1(self.d1)
        
            