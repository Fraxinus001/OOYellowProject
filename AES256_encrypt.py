import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2


def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '


def get_private_key(password):
    salt = b"12345dfgrgss"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    print(cipher.encrypt(raw))
    return base64.b64encode(bytes(str(iv + cipher.encrypt(raw))))
