import pickle
import base64

# Amaii~ Baniraanii~
VanillaSalt = b"12345dfgrgs"
Dumping = base64.b64encode(VanillaSalt)

def write(data):
    return open(data, "wb")


pickle.dump(Dumping, write("IDCSys_0x001.pvk"), pickle.HIGHEST_PROTOCOL)
