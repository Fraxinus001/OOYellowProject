
import pickle
import datetime
import base64
import AES256_synth
from collections import defaultdict


class IDCSys_Database:
    def __init__(self):
        DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        dat001 = self.readmode("dat001.db")
        dat002 = self.readmode("dat002.db")
        dat003 = self.readmode("dat003.db")
        dat004 = self.readmode("dat004.db")
        d1 = pickle.load(dat001)
        d2 = pickle.load(dat002)
        d3 = pickle.load(dat003)
        d4 = pickle.load(dat004)
    
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
        
    
class IDCSys_Database_Test(IDCSys_Database):
    def __init__(self):
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

        
        
class IDCSys_Database_Reset(IDCSys_Database):
    def __init__(self):
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        
    def gen_UUID(self):
        self.UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
        return self.UUID
    
    def maintemplate(self):
        UUID = self.gen_UUID()
        return {UUID: []}
    
    def execwrite_a(self, dat):
        self.w_dump(self.maintemplate, dat)
        self.f_close(dat)
    
    def execwrite(self):
        self.maintemplate = self.maintemplate()
        #print(self.maintemplate)
        a = self.writemode("dat001.db")
        b = self.writemode("dat002.db")
        c = self.writemode("dat003.db")
        d = self.writemode("dat004.db")
        self.execwrite_a(a), self.execwrite_a(b), self.execwrite_a(c), self.execwrite_a(d)

        load_a = pickle.load(self.readmode("dat001.db"))
        load_b = pickle.load(self.readmode("dat002.db"))
        load_c = pickle.load(self.readmode("dat003.db"))
        load_d = pickle.load(self.readmode("dat004.db"))
        print(f"debug: {load_a}")
        print(f"debug: {load_b}")
        print(f"debug: {load_c}")
        print(f"debug: {load_d}")
        

print(IDCSys_Database_Reset().execwrite())
