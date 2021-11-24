
import pickle
import datetime
import base64
import AES256_synth
from collections import defaultdict


class IDCSys_Database:
    def __init__(self):
        DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        #dat001 = self.readmode("dat001.db")
        #dat002 = self.readmode("dat002.db")
        #dat003 = self.readmode("dat003.db")
        #dat004 = self.readmode("dat004.db")
        #d1 = pickle.load(dat001)
        #d2 = pickle.load(dat002)
        #d3 = pickle.load(dat003)
        #d4 = pickle.load(dat004)
    
    def readmode(self, data):
        return open(data, "rb")
    
    def writemode(self, data):
        return open(data, "wb")
    
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

    def dump(self):
        self.d1a
        
        
class IDCSys_Database_Reset(IDCSys_Database):
    def __init__(self):
        self.DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        
    def gen_UUID(self):
        self.UUID = AES256_synth.KeyEncrypt(self.DateTimeNow).KeyEncrypt()
        return self.UUID
    
    def maintemplate(self):
        UUID = self.gen_UUID()
        return {UUID:[]}
    
    def execwrite(self):
        self.maintemplate = self.maintemplate()
        self.writemode = self.writemode("dat001.db")
        self.w_dump(self.maintemplate, self.writemode)
        print(self.maintemplate)
        a = pickle.load(self.readmode("dat001.db"))
        print(f"debug: {a}")

print(IDCSys_Database_Reset().execwrite())
