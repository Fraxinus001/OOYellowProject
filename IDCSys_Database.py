# pip install cryptography

import pickle
import datetime
import base64
import AES256_synth
from collections import defaultdict
from cryptography.fernet import Fernet


class IDCSys_Database:
    def __init__(self):
        # For DEMO purposes:
        self.UUID_DEMO = b'h9HpeoZ5V0QR+CRR2bvTHQ9Qu1M/zSe0ESQEfFqUfkQJrViZuwdA3o68PpNl4JHjsx2La3B5JyyG25NSRkI+cw=='

        self.serialk = "0000-00000-000"
        self.fernet = Fernet(self.load_FernetKey())
        FernetKey = None
        self.dat001 = self.readmode("dat001.db")
        self.dat002 = self.readmode("dat002.db")
        self.dat003 = self.readmode("dat003.db")
        self.dat004 = self.readmode("dat004.db")
        self.d1 = pickle.load(self.dat001)
        self.d2 = pickle.load(self.dat002)
        self.d3 = pickle.load(self.dat003)
        self.d4 = pickle.load(self.dat004)
    
    def load_FernetKey(self):
        key = AES256_synth.FernetKey(AES256_synth).FernetKey()
        return key
    
    def KeyEncrypt(self, key):
        return AES256_synth.KeyEncrypt(key).KeyEncrypt()
    
    def KeyDecrypt_utf(self, key):
        return AES256_synth.KeyDecrypt(AES256_synth).KeyDecrypt(key).decode('utf-8')
        
    def KeyDecrypt_byt(self, key):
        return AES256_synth.KeyDecrypt(AES256_synth).KeyDecrypt(key)
    
    def gen_UUID(self):
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        AccessKey = f"IDCSys-<{self.DateTimeNow}>-sySCDI"
        self.UUID = AES256_synth.KeyEncrypt(AccessKey).KeyEncrypt()
        return self.UUID
    
    def readmode(self, file):
        return open(file, "rb")
    
    def writemode(self, file):
        return open(file, "wb")
    
    def loadsection(self, a, b):
        S = {a: b}
        return S
    
    def w_addrecord(self, dx, a, x, y):
        for key in dict(dx):
            if key == a:
                dx[a].append(x)
                dx[a][x] = y
                
    def w_addreg(self, dx, key, val):
        dx[key] = val
    
    def w_pop_(self, dx, UUID, input1):
        dx[UUID] = dx.pop(input1)
        
    def w_change_001(self, dx, UUID, A, index1, B):
        a = dx[UUID].index(A)
        b = dx[UUID][a]
        dx[UUID][index1].pop(B)
        return
    
    def w_update(self, f, dx):
        dx.update(f)
        
    def w_dump(self, dx, data):
        pickle.dump(dx, data)
        
    def f_load(self, dx):
        return pickle.load(dx)
        
    def f_close(self, dx):
        dx.close()
        
    def f_dump_dx(self, d1):
        with self.writemode("dat001.db") as db:
            self.w_dump(d1, db)
        
    def f_readmode_all(self):
        self.dat001 = self.readmode("dat001.db")
        self.dat002 = self.readmode("dat002.db")
        self.dat003 = self.readmode("dat003.db")
        self.dat004 = self.readmode("dat004.db")
        self.d1 = pickle.load(self.dat001)
        self.d2 = pickle.load(self.dat002)
        self.d3 = pickle.load(self.dat003)
        self.d4 = pickle.load(self.dat004)
        
    def f_writemode_all(self):
        self.dat001 = self.writemode("dat001.db")
        self.dat002 = self.writemode("dat002.db")
        self.dat003 = self.writemode("dat003.db")
        self.dat004 = self.writemode("dat004.db")
        self.d1 = pickle.load(self.dat001)
        self.d2 = pickle.load(self.dat002)
        self.d3 = pickle.load(self.dat003)
        self.d4 = pickle.load(self.dat004)
        
    def f_dump_all(self, d1, d2, d3, d4):
        pickle.dump(d1, self.dat001)
        pickle.dump(d2, self.dat002)
        pickle.dump(d3, self.dat003)
        pickle.dump(d4, self.dat004)
        
    def f_close_all(self):
        self.d1.close(), self.d2.close(), self.d3.close(), self.d4.close()
        
class IDCSys_Database_Reset(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.DateTimeNow = None
        self.UUID = None
        self.maintemplate = self.maintemplate()
        
    def gen_UUID(self):
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        AccessKey = f"IDCSys-<{self.DateTimeNow}>-sySCDI"
        self.UUID = AES256_synth.KeyEncrypt(AccessKey).KeyEncrypt()
        return self.UUID
    
    def maintemplate(self):
        UUID = self.gen_UUID()
        return {UUID: []}
    
    def execwrite_a(self, dat):
        with self.writemode(dat) as opf1:
            self.w_dump(self.maintemplate, opf1)
        #self.fernet = Fernet(self.load_FernetKey())
        enc = self.fernet.encrypt(self.readmode(dat).read())
        self.readmode(dat).close()
        #self.writemode(dat).write(enc)
        
    def execwrite(self):
        #print(f"debug: {self.maintemplate}")
        a = "dat001.db"
        b = "dat002.db"
        c = "dat003.db"
        d = "dat004.db"
        self.execwrite_a(a), self.execwrite_a(b), self.execwrite_a(c), self.execwrite_a(d)
        print(type(self.readmode("dat001.db").read()))
        load_a = pickle.load(self.readmode("dat002.db"))
        load_b = pickle.load(self.readmode("dat002.db"))
        load_c = pickle.load(self.readmode("dat003.db"))
        load_d = pickle.load(self.readmode("dat004.db"))
        print(f"debug: {load_a}")
        print(f"debug: {load_b}")
        print(f"debug: {load_c}")
        print(f"debug: {load_d}")


class IDCSys_Database_Test(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.d1a = {b'rWOmY9hR0FwFRVrlRYKEyjH4jq+Yj6ZKlzCNKNwRnsxxFKQrjojVYb7QjtQyuIz+': [b'Raf', b'Dec. 8, 2020']}
        usr1 = b'rWOmY9hR0FwFRVrlRYKEyjH4jq+Yj6ZKlzCNKNwRnsxxFKQrjojVYb7QjtQyuIz+'
        print(f"debug: {self.d1a[usr1]}")
        print(f"debug: {self.d1a[usr1][0]}")
        self.d1a[usr1][0] = base64.b64encode(self.d1a[usr1][0])
        self.d1a[usr1][1] = base64.b64encode(self.d1a[usr1][1])
        print(f"debug: {self.d1a}")
        self.d1a[usr1][0] = base64.b64decode(self.d1a[usr1][0])
        self.d1a[usr1][1] = base64.b64decode(self.d1a[usr1][1])
        print(f"debug: {self.d1a}")
        self.d1a[usr1][0] = self.d1a[usr1][0].decode()
        self.d1a[usr1][1] = self.d1a[usr1][1].decode()
        print(f"debug: {self.d1a}")
        

# if __name__ == '__main__':
# IDCSys_Database_Reset().execwrite()
