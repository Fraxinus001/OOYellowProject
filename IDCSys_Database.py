
import pickle
import datetime
from collections import defaultdict


class IDCSys_Database():
    def __init__(self):
        Datenow = datetime.date.today().strftime("%B %d, %Y")
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
    
class IDCSys_Database_Reset():
    def __init__(self):
        Datenow = datetime.date.today().strftime("%B %d, %Y")
        
    