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
        self.permissions = {}  # load_perms
    
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


class IDCSys_Authorizor_BuildDB(IDCSys_Database):
    def __init__(self):
        super().__init__()
        # self.DateTimeNow - Used to generate encryption keys.
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        self.UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
        self.enc_ty = self.KeyEncrypt('degty@idcsys.com')
        self.enc_ta = self.KeyEncrypt('fstale@idcsys.com')
        self.template_a = self.template_a()
        self.template_b = self.template_b()
        self.template_c = self.template_c()
        
    def add_user(self):
        a = self.writemode("dat0A1.db")
        inputusn = input("Please enter the username: ")
        inputpas = input("Please enter the password: ")
        authenticator.add_user(inputusn, inputpas)
        # User(inputusn, inputpas).return_usn()
        self.f_close(a)
    
    def load_users(self):
        load_usrland = pickle.load(self.readmode("dat0A1.db"))
        return load_usrland
    
    def template_a(self):
        return {self.enc_ty: self.KeyEncrypt('12345@sae2'),
                self.enc_ta: self.KeyEncrypt('12345@sae2')}
    
    def template_b(self):
        return {self.KeyEncrypt('Read'): [self.enc_ty, self.enc_ta],
                self.KeyEncrypt('Write'): [self.enc_ty, self.enc_ta],
                self.KeyEncrypt('Delete'): [self.enc_ty, self.enc_ta],
                self.KeyEncrypt('Modify'): [self.enc_ty, self.enc_ta]}
    
    def template_c(self):
        return {self.enc_ty: self.KeyEncrypt('Ty, Dominic Edward, Garchitorena'),
                self.enc_ta: self.KeyEncrypt('Tale, Francis, Sales')}
    
    def execwrite_a(self, dat):
        self.w_dump(self.template_a, dat)
        self.f_close(dat)
    
    def execwrite_b(self, dat):
        self.w_dump(self.template_b, dat)
        self.f_close(dat)
        
    def execwrite_c(self, dat):
        self.w_dump(self.template_c, dat)
        self.f_close(dat)
    
    def execwrite(self):
        print(self.enc_ta)
        # print(f"debug: {self.template_a}")
        a = self.writemode("dat0A1.db")
        self.execwrite_a(a)
        # load_a = pickle.load(self.readmode("dat0A1.db"))
        # print(f"debug: {load_a}")
        b = self.writemode("dat0A2.db")
        self.execwrite_b(b)
        # load_b = pickle.load(self.readmode("dat0A2.db"))
        # print(f"debug: {load_b}")
        c = self.writemode("dat0A3.db")
        self.execwrite_c(c)
        # load_c = pickle.load(self.readmode("dat0A3.db"))
        # print(f"debug: {load_c}")


class Authorize(IDCSys_Database):
    def load_users(self):
        load_usrland = pickle.load(self.readmode("dat0A1.db"))
        return load_usrland
    
    def load_perms(self):
        load_permsland = pickle.load(self.readmode("dat0A2.db"))
        return load_permsland
    
    def load_names(self):
        load_namesland = pickle.load(self.readmode("dat0A3.db"))
        return load_namesland

    def dat0A1_Load(self):
        for keys in self.load_users().keys():
            authenticator.add_user(self.KeyDecrypt_utf(keys), self.KeyDecrypt_utf(self.load_users()[keys]))
            
    def dat0A2_Load(self):
        for keys in self.load_perms().keys():
            authorizor.add_permission(self.KeyDecrypt_byt(keys))
            for user in self.load_perms()[keys]:
                authorizor.permit_user(self.KeyDecrypt_byt(keys), self.KeyDecrypt_utf(user))
    
    def run(self):
        # IDCSys_Authorizor_BuildDB().execwrite()
        self.dat0A1_Load()
        self.dat0A2_Load()

# Authorize().run()
