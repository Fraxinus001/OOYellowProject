import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


def unpad(s):
    return s[0:-ord(s[-1:])]


def get_private_key(password, salt):
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def KeyDecrypt(enc, password, salt):
    private_key = get_private_key(password, salt)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
