# ID Centralization System

import AES256_synth
import IDCSys_Database
import IDCSys_Authorizor


class IDCSys_Core:
    def __init__(self):
        self.authenticator = IDCSys_Authorizor.authenticator
        self.authorizor = IDCSys_Authorizor.authorizor
        self.UUID = "IDCSys-<TestPass02>-sySCDI"
        self.AES_1 = AES256_synth.KeyEncrypt
        self.AES_2 = AES256_synth.KeyDecrypt
        self.username = 'User'
        self.menu_map = {
            "login": self.login,
            "finda": self.finda,
            "find": self.find,
            "new": self.new,
            "change": self.change,
            "serial": self.serial,
            "quit": self.quit,
        }
        
    # Login
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = self.authenticator.login(username, password)
            except IDCSys_Authorizor.InvalidUsername:
                print("Sorry, that username does not exist")
            except IDCSys_Authorizor.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
        
    def is_permitted(self, permission):
        try:
            self.authorizor.check_permission(permission, self.username)
        except IDCSys_Authorizor.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except IDCSys_Authorizor.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True
        
    # Display Serial no.
    def serial(self):
        if self.is_permitted(b"Read"):
            print(f"serial:")
        else:
            print(f"Access Denied.")
        
    # Find (Auto)
    def finda(self):
        if self.is_permitted(b"Modify"):
            print(f"To find(auto)")
        else:
            print(f"Access Denied.")
            
    # Find
    def find(self):
        print(f"To find")
        if self.is_permitted(b"Modify"):
            print()
        else:
            print(f"Access Denied.")
            
    # New Record
    def new(self):
        if self.is_permitted(b"Modify"):
            print(f"To create new")
        else:
            print(f"Access Denied.")
    
    # Change
    def change(self):
        if self.is_permitted(b"Modify"):
            print(f"To change")
        else:
            print(f"Access Denied.")
            
    # AES_256
    def IDCSys_Encrypt(self):
        EncryptDat = self.AES_1(self.UUID).KeyEncrypt()
        print(f"debug: {EncryptDat}")
        return EncryptDat
        
    def IDCSys_Decrypt(self):
        print(f"debug: {self.AES_2('').KeyDecrypt(self.AES_1(self.UUID).KeyEncrypt())}")
        
    # Quit
    def quit(self):
        raise SystemExit()
    
    # Main Menu
    def mainmenu_console(self):
        print("Welcome to ID Centralization System")
        if self.UUID != '':
            print(f"debug: Running!")
            try:
                answer = ""
                while True:
                    print("""
Please enter a command:
\tlogin\tLogin
\tfinda\tFind Record(s) (Automated)
\tfind\tFind Record(s) (Manual Search)
\tnew \tAdd new Record(s)
\tchange\tChange existing record(s)
\tserial\tPrint Serial No.
\tquit\tQuit
                          """)
                    answer = input("enter a command: ").lower()
                    try:
                        func = self.menu_map[answer]
                    except KeyError:
                        print("{} is not a valid option".format(answer))
                    else:
                        func()
            finally:
                print("Thank you.")
        else:
            print(f"debug: failing..")


if __name__ == '__main__':
    IDCSys_Authorizor.Authorize().run()
    #IDCSys_Core().IDCSys_Encrypt()
    #IDCSys_Core().IDCSys_Decrypt()
    IDCSys_Core().mainmenu_console()
