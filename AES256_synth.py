# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt

password = "12345"
encdat1 = 'TESTPASS1'

KeyEncrypt = AES256_encrypt.KeyEncrypt(encdat1, password)
print(KeyEncrypt)

KeyDecrypt = AES256_decrypt.KeyDecrypt(KeyEncrypt, password)
print(KeyDecrypt)