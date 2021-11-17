# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt

password = "12345"
AccessKey = 'TESTPASS1'

KeyEncrypt = AES256_encrypt.KeyEncrypt(AccessKey, password)
print(KeyEncrypt)

KeyDecrypt = AES256_decrypt.KeyDecrypt(KeyEncrypt, password)
print(KeyDecrypt)