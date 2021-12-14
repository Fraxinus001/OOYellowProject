# pip install cryptography

import pickle
import datetime
import AES256_synth


class IDCSys_Database:
    def __init__(self):
        # For DEMO purposes, update this everytime is reset:
        self.UUID_DEMO = b'ulLbkB+16haTlO2R81F3q5Y3lMjbCTEaFR54U97R1eIp12PaFOucvEN3a//R9JpLf5LpYNXYQV8jDQaFw1UAxg=='

        self.serialk = "0000-00000-000"
        self.dat001 = self.readmode("dat001.db")
        self.dat002 = self.readmode("dat002.db")
        self.dat003 = self.readmode("dat003.db")
        self.dat004 = self.readmode("dat004.db")
        self.d1 = pickle.load(self.dat001)
        self.d2 = pickle.load(self.dat002)
        self.d3 = pickle.load(self.dat003)
        self.d4 = pickle.load(self.dat004)
    
    @staticmethod
    def KeyEncrypt(key):
        return AES256_synth.KeyEncrypt(key).KeyEncrypt()

    @staticmethod
    def KeyDecrypt_utf(key):
        return AES256_synth.KeyDecrypt(AES256_synth).KeyDecrypt(key).decode('utf-8')

    @staticmethod
    def KeyDecrypt_byt(key):
        return AES256_synth.KeyDecrypt(AES256_synth).KeyDecrypt(key)
    
    @staticmethod
    def gen_UUID():
        DateTimeNow = datetime.datetime.today().strftime("%B %d, %Y - %I:%M:%S%p")
        AccessKey = f"IDCSys-<{DateTimeNow}>-sySCDI"
        UUID = AES256_synth.KeyEncrypt(AccessKey).KeyEncrypt()
        return UUID

    @staticmethod
    def readmode(file):
        return open(file, "rb")

    @staticmethod
    def writemode(file):
        return open(file, "wb")

    @staticmethod
    def loadsection(a, b):
        S = {a: b}
        return S

    @staticmethod
    def w_addrecord(dx, a, y, z):
        list = []
        for key in dict(dx):
            list.append(key)
        if a in list:
            try:
                if dx[a][z] in dx[a]:
                    dx[a].pop(z)
                    dx[a].insert(z, y)
                if dx[a][z] not in dx[a]:
                    dx[a].append(y)
            except IndexError:
                dx[a].append(y)
        if a not in list:
            di = {a: []}
            dx.update(di)
            dx[a].append(y)

    @staticmethod
    def w_addreg(dx, key, val):
        dx[key] = val

    @staticmethod
    def w_pop_(dx, key):
        dx.pop(key)

    @staticmethod
    def w_update(f, dx):
        dx.update(f)

    @staticmethod
    def w_dump(dx, data):
        pickle.dump(dx, data)

    @staticmethod
    def f_load(dx):
        return pickle.load(dx)

    @staticmethod
    def f_close(dx):
        dx.close()
        
    def f_dump_d1(self, d1):
        with self.writemode("dat001.db") as db:
            self.w_dump(d1, db)
            
    def f_dump_d2(self, d2):
        with self.writemode("dat002.db") as db:
            self.w_dump(d2, db)
            
    def f_dump_d3(self, d3):
        with self.writemode("dat003.db") as db:
            self.w_dump(d3, db)
            
    def f_dump_d4(self, d4):
        with self.writemode("dat004.db") as db:
            self.w_dump(d4, db)
        
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
        self.readmode(dat).close()
        
    def execwrite(self):
        # print(f"debug: {self.maintemplate}")
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
        

# if __name__ == '__main__':
 # IDCSys_Database_Reset().execwrite()
