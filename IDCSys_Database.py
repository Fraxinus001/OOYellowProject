# pip install cryptography

import pickle
import datetime
import base64
import AES256_synth
from collections import defaultdict
from cryptography.fernet import Fernet


class IDCSys_Database:
    def __init__(self):
        DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        self.fernet = Fernet(self.load_FernetKey())
        FernetKey = None
        #dat001 = fernet.decrypt(self.readmode("dat001.db").read())
        #dat002 = fernet.decrypt(self.readmode("dat002.db").read())
        #dat003 = fernet.decrypt(self.readmode("dat003.db").read())
        #dat004 = fernet.decrypt(self.readmode("dat004.db").read())
        #d1 = pickle.load(dat001)
        #d2 = pickle.load(dat002)
        #d3 = pickle.load(dat003)
        #d4 = pickle.load(dat004)
    
    def load_FernetKey(self):
        key = AES256_synth.FernetKey(AES256_synth).FernetKey()
        return key
    
    def readmode(self, file):
        return open(file, "rb")
    
    def writemode(self, file):
        return open(file, "wb")
    
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
        
    def f_close(self, dx):
        dx.close()
        
class IDCSys_Database_Reset(IDCSys_Database):
    def __init__(self):
        super().__init__()
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        self.UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
        self.maintemplate = self.maintemplate()
        
    def gen_UUID(self):
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
        

#if __name__ == '__main__':
    print(IDCSys_Database_Reset().execwrite())
