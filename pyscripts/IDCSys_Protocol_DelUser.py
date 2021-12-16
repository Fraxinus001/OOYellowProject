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
        print("\033[95mAdministration: Delete user account\033[0m")
        print("Please login again to continue.")
        IDCSys_Core.IDCSys_Core().logged_in = False
        IDCSys_Core.IDCSys_Core().login()
        input("Please press any key to continue.")
        print("\033[95mAuthorization:\033[0m")
        FN = input("Please input the registrant's First Name: ")
        MN = input("Please input the registrant's Middle Name: ")
        LN = input("Please input the registrant's Last Name: ")
        self.name = LN + ", " + FN + ", " + MN
        ans = None
        try:
            for i in self.dA3:
                if self.KeyDecrypt_utf(self.dA3[i]) == self.name:
                    ans = input(f"Are you sure you want to delete {self.name} from the users database? (yes or no)") or "no"
        except RuntimeError:
            print("Specified name was not found in the users' database.")
        if ans == "yes":
            try:
                for i in self.dA3:
                    if self.KeyDecrypt_utf(self.dA3[i]) == self.name:
                        self.username = i
                        self.dA3.pop(i)
            except RuntimeError:
                pass
            try:
                for i in self.dA1:
                    if i == self.username:
                        self.dA1.pop(i)
            except RuntimeError:
                pass
            try:
                for i in self.dA2:
                    if self.KeyDecrypt_utf(i) == 'Write':
                        for j in self.dA2[i]:
                            if j == self.username:
                                self.dA2[i].pop(self.dA2[i].index(j))
            except RuntimeError:
                pass
            try:
                for i in self.dA2:
                    if self.KeyDecrypt_utf(i) == 'Modify':
                        for j in self.dA2[i]:
                            if j == self.username:
                                self.dA2[i].pop(self.dA2[i].index(j))
                                pass
            except RuntimeError:
                pass
            try:
                for i in self.dA2:
                    if self.KeyDecrypt_utf(i) == 'Delete':
                        for j in self.dA2[i]:
                            if j == self.username:
                                self.dA2[i].pop(self.dA2[i].index(j))
                                pass
            except RuntimeError:
                pass
            try:
                for i in self.dA2:
                    if self.KeyDecrypt_utf(i) == 'Read':
                        for j in self.dA2[i]:
                            if j == self.username:
                                self.dA2[i].pop(self.dA2[i].index(j))
                                pass
            except RuntimeError:
                pass
            print("///  END OF QUERY  ///")
            x = self.writemode("dat0A1.db")
            self.w_dump(self.dA1, x)
            self.f_close(x)
            x = self.writemode("dat0A2.db")
            self.w_dump(self.dA2, x)
            self.f_close(x)
            x = self.writemode("dat0A3.db")
            self.w_dump(self.dA3, x)
            self.f_close(x)
            print("\033[95mThe user was removed from the database\033[0m")
            ans = input("\033[95mRestart the program to apply changes? (yes or no) \033[0m")
            if ans == "yes":
                raise SystemExit()
            else:
                pass
            input("\033[95mPlease press any key to continue.\033[0m")
        else:
            print("Now going back to main menu.")
            input("\033[95mPlease press any key to continue.\033[0m")
            pass
