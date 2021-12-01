import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2

BLOCK_SIZE = 16
pad = lambda s: bytes(s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE), 'utf-8')


def get_private_key(password, salt):
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def KeyEncrypt(raw, password, salt):
    print(f"debug: {salt}")
    private_key = get_private_key(password, salt)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
