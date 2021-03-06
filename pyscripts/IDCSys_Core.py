# ID Centralization System
# Prerequisites: pip install pycryptodomex
# Prerequisites: pip install cryptography
# install in Pycharm File -> Settings -> Project -> Python Interpreter

import IDCSys_Authorizor
import IDCSys_Protocol_NewRecord
import IDCSys_Protocol_ModifyRecord
import IDCSys_Protocol_RegUser
import IDCSys_Protocol_DelUser
import IDCSys_Protocol_Find_Auto
import IDCSys_Protocol_Find_Manual
import IDCSys_Protocol_ShowUsers
from IDCSys_Database import IDCSys_Database


# Main Menu class for our Program.
class IDCSys_Core(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.authenticator = IDCSys_Authorizor.authenticator
        self.authorizor = IDCSys_Authorizor.authorizor
        self.dat0A3 = self.readmode("dat0A3.db")
        self.dA3 = self.f_load(self.dat0A3)
        self.UUID = None
        self.logged_in = False
        self.username = 'User'
        # Menu Mappings Initialization
        self.menu_map = {
            "login": self.login,
            "admin": self.admin,
            "finda": self.finda,
            "find": self.find,
            "new": self.new,
            "change": self.change,
            "serial": self.serial,
            "quit": self.quit,
        }
        self.menu_map_admin = {
            "1": self.logout,
            "2": self.dispusr,
            "3": self.reg,
            "4": self.del_user,
            "5": self.back,
        }
        
    # Function call for login permission checks.
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
    @staticmethod
    def serial():
        print(f"Serial No.: {IDCSys_Database().serialk}")

    # Function call for Admin menu
    def admin(self):
        print("""
\t\033[95m1\t\033[0mLogout
\t\033[95m2  \t\033[0mDisplay user accounts
\t\033[95m3  \t\033[0mRegister new user
\t\033[95m4  \t\033[0mDelete user
\t\033[95m5\t\033[0mGo Back
                          """)
        answer = input("Please enter a command: ").lower()
        try:
            func = self.menu_map_admin[answer]
        except KeyError:
            print("{} is not a valid option".format(answer))
        else:
            func()

    # Function call for Who Is Logged In
    def whois_logged_in(self):
        for i in self.dA3:
            if self.KeyDecrypt_utf(i) == self.username:
                return self.KeyDecrypt_utf(self.dA3[i])
        
    # Function call for Login
    def login(self):
        while not self.logged_in:
            username = input("Username: ")
            password = input("Password: ")
            if username == "DEMO" or username == "":
                username = "fstale@idcsys.com"
                password = "12345@sae2"
            try:
                self.logged_in = self.authenticator.login(username, password)
            except IDCSys_Authorizor.InvalidUsername:
                print("Sorry, that username does not exist")
            except IDCSys_Authorizor.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
            if username == "fstale@idcsys.com" and self.logged_in is True:
                print("Demonstration Mode. Auto logged-in with full Administration\n"
                      "rights.")

    # Function call for Logout
    def logout(self):
        while self.logged_in:
            self.username = 'User'
            self.password = None
            self.logged_in = False
        print("You have just logged out.")
        input("Press any key to continue.")
        pass

    # Function call for Display User
    def dispusr(self):
        if self.is_permitted(b"Read"):
            IDCSys_Protocol_ShowUsers.Protocol.menu(IDCSys_Protocol_ShowUsers.Protocol())
        else:
            print(f"Access Denied.")

    # Function call for Register New User
    def reg(self):
        if self.is_permitted(b"Write"):
            IDCSys_Protocol_RegUser.Protocol().menu()
        else:
            print(f"Access Denied.")
            
    def del_user(self):
        if self.is_permitted(b"Delete"):
            IDCSys_Protocol_DelUser.Protocol().menu()
        else:
            print(f"Access Denied.")
        
    # Find (Auto)
    def finda(self):
        if self.is_permitted(b"Read"):
            IDCSys_Protocol_Find_Auto.Protocol.menu(IDCSys_Protocol_Find_Auto.Protocol())
        else:
            print(f"Access Denied.")
            
    # Find
    def find(self):
        if self.is_permitted(b"Read"):
            IDCSys_Protocol_Find_Manual.Protocol.menu(IDCSys_Protocol_Find_Manual.Protocol())
        else:
            print(f"Access Denied.")
            
    # New Record
    def new(self):
        if self.is_permitted(b"Write"):
            IDCSys_Protocol_NewRecord.Protocol.menu(IDCSys_Protocol_NewRecord.Protocol())
        else:
            print(f"Access Denied.")
    
    # Change
    def change(self):
        if self.is_permitted(b"Modify"):
            IDCSys_Protocol_ModifyRecord.Protocol.menu(IDCSys_Protocol_ModifyRecord.Protocol())
        else:
            print(f"Access Denied.")
        
    def back(self):
        pass
    
    # Quit
    @staticmethod
    def quit():
        print("Thank you for using our program.")
        print("This program was built by Dominic Edward G. Ty and Francis S. Tale.")
        print("Project submission to Sir Ramon Stephen L. Ruiz of \n"
              "Don Bosco Technical College - Mandaluyong.")
        raise SystemExit()
    
    def mainmenu_func_login(self):
        if self.logged_in:
            return f"""\t\033[95mLogged in as {self.whois_logged_in()}\033[0m
\t\033[95madmin\t\033[0mAdministration"""
        if not self.logged_in:
            return "\t\033[95mlogin\t\033[0mLogin"
    
    # Main Menu
    def mainmenu_console(self):
        print("Welcome to ID Centralization System")
        while True:
            print(f"""
{self.mainmenu_func_login()}
\t\033[95mfinda\t\033[0mFind Record(s) (Automated)
\t\033[95mfind\t\033[0mFind Record(s) (Manual Search)
\t\033[95mnew \t\033[0mAdd new Record(s)
\t\033[95mchange\t\033[0mChange existing record(s)
\t\033[95mserial\t\033[0mPrint Serial No.
\t\033[95mquit\t\033[0mQuit
                  """)
            answer = input("Please enter a command: ").lower()
            try:
                func = self.menu_map[answer]
            except KeyError:
                print("{} is not a valid option".format(answer))
            else:
                func()


if __name__ == '__main__':
    IDCSys_Authorizor.Authorize().run()
    IDCSys_Core().mainmenu_console()
