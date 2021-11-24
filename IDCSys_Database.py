
import pickle
import datetime
import base64
from collections import defaultdict


class IDCSys_Database:
    def __init__(self):
        DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        d1 = self.read("dat001.db")
        d2 = self.read("dat002.db")
        d3 = self.read("dat003.db")
        d4 = self.read("dat004.db")
        dat001 = pickle.load(d1)
        dat002 = pickle.load(d2)
        dat003 = pickle.load(d3)
        dat004 = pickle.load(d4)
    
    def read(self, data):
        return open(data, "rb")
    
    def write(self, data):
        return open(data, "wb")
    
class IDCSys_Database_Reset(IDCSys_Database):
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
        
IDCSys_Database_Reset()