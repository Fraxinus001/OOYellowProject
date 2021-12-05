import hashlib
import AES256_synth
import pickle
import datetime
from IDCSys_Database import IDCSys_Database


class User:
    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False
    
    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
    
    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password
    
    def return_usn(self):
        return self.username
    
    def return_pas(self):
        return self.password


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class Authenticator:
    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""
        self.users = {}
    
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
    
    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True
    
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
    
    def return_users(self):
        return self.users


class Authorizor(IDCSys_Database):
    def __init__(self, authenticator):
        super().__init__()
        self.authenticator = authenticator
        #load_perms = pickle.load(self.readmode("dat000.db"))
        self.permissions = {} #load_perms
    
    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")
    
    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)
    
    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

    def return_perms(self):
        return self.permissions


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


authenticator = Authenticator()
authorizor = Authorizor(authenticator)


class Authority:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = authenticator.login(username, password)
            except InvalidUsername:
                print("Sorry, that username does not exist")
            except InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
    
    def is_permitted(self, permission):
        try:
            authorizor.check_permission(permission, self.username)
        except NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True
    
    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")
    
    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")
    
    def quit(self):
        raise SystemExit()
    
    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
                    Please enter a command:
                    \tlogin\tLogin
                    \ttest\tTest the program
                    \tchange\tChange the program
                    \tquit\tQuit
                    """
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


class IDCSys_Authorizor_BuildDB(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        self.UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
        self.template_a = self.template_a()
        self.template_b = self.template_b()
        
    def add_user(self):
        a = self.writemode("dat0A1.db")
        load_usrland = pickle.load(a)
        inputusn = input("Please enter the username: ")
        inputpas = input("Please enter the password: ")
        authenticator.add_user(inputusn, inputpas)
        #User(inputusn, inputpas).return_usn()
        self.f_close(a)
    
    def load_users(self):
        load_usrland = pickle.load(self.readmode("dat0A1"))
        return load_usrland
    
    def template_a(self):
        return {'degty@idcsys.com': '33d76d30cdc8108b67aca1e1a2a579720b9a13746651ac84d7b85272e3b6d7fa',
                'fstale@idcsys.com': '33d76d30cdc8108b67aca1e1a2a579720b9a13746651ac84d7b85272e3b6d7fa'}
    
    def template_b(self):
        return {b'Read': {'degty@idcsys.com', 'fstale@idcsys.com'},
                 b'Write': {'degty@idcsys.com', 'fstale@idcsys.com'},
                 b'Delete': {'degty@idcsys.com', 'fstale@idcsys.com'},
                 b'Modify': {'degty@idcsys.com', 'fstale@idcsys.com'}}
    
    def execwrite_a(self, dat):
        self.w_dump(self.template_a, dat)
        self.f_close(dat)
    
    def execwrite_b(self, dat):
        self.w_dump(self.template_b, dat)
        self.f_close(dat)
    
    def execwrite(self):
        # print(f"debug: {self.template_a}")
        a = self.writemode("dat0A1.db")
        self.execwrite_a(a)
        load_a = pickle.load(self.readmode("dat0A1.db"))
        print(f"debug: {load_a}")
        b = self.writemode("dat0A2.db")
        self.execwrite_b(b)
        load_b = pickle.load(self.readmode("dat0A2.db"))
        print(f"debug: {load_b}")

        


class Authorize:
    def run(self):
        IDCSys_Authorizor_BuildDB().execwrite()
        # Set up a test user and permission
        # Permits to operate
        authorizor.add_permission(b"Read")
        authorizor.add_permission(b"Write")
        authorizor.add_permission(b"Delete")
        authorizor.add_permission(b"Modify")
        #print(Authenticator().return_users())
        #print(authorizor.return_perms())
        
        
        
        # Dominic Edward G. Ty
        authenticator.add_user("degty@idcsys.com", "12345@sae2")
        authorizor.permit_user(b"Read", "degty@idcsys.com")
        authorizor.permit_user(b"Write", "degty@idcsys.com")
        authorizor.permit_user(b"Delete", "degty@idcsys.com")
        authorizor.permit_user(b"Modify", "degty@idcsys.com")
        print(User("degty@idcsys.com", "12345@sae2").return_usn())
        print(User("degty@idcsys.com", "12345@sae2").return_pas())
        # Francis S. Tale
        authenticator.add_user("fstale@idcsys.com", "12345@sae2")
        authorizor.permit_user(b"Read", "fstale@idcsys.com")
        authorizor.permit_user(b"Write", "fstale@idcsys.com")
        authorizor.permit_user(b"Delete", "fstale@idcsys.com")
        authorizor.permit_user(b"Modify", "fstale@idcsys.com")
        #print(Authenticator().return_users())
        #print(authorizor.return_perms())
