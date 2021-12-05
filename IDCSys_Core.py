# ID Centralization System

import AES256_synth
import IDCSys_Authorizor
import IDCSys_Protocol_NewRecord


class IDCSys_Core:
    def __init__(self):
        self.authenticator = IDCSys_Authorizor.authenticator
        self.authorizor = IDCSys_Authorizor.authorizor
        self.UUID = b'PQVNe7ZhcwqnkW4cUI+/UfpSo4DO9gj52h4ah+gNbjrJzyrYr4sM41T5LBTR7t/5'
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
            print(username)
            if username == "DEMO" or username == "":
                username = "fstale@idcsys.com"
                password = "12345@sae2"
                print("Demonstration Mode. Auto logged-in with full Administration\n"
                      "rights.")
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
            IDCSys_Protocol_NewRecord.protocol.menu(IDCSys_Protocol_NewRecord.protocol(self.UUID))
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
\t\033[95mlogin\t\033[0mLogin
\t\033[95mfinda\t\033[0mFind Record(s) (Automated)
\t\033[95mfind\t\033[0mFind Record(s) (Manual Search)
\t\033[95mnew \t\033[0mAdd new Record(s)
\t\033[95mchange\t\033[0mChange existing record(s)
\t\033[95mserial\t\033[0mPrint Serial No.
\t\033[95mquit\t\033[0mQuit
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
