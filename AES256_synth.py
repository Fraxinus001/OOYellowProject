# pip install pycryptodomex

import AES256_encrypt
import AES256_decrypt

password = "12345"

encrypted = AES256_encrypt.encrypt("TESTPASSWORD1", password)
print(encrypted)

decrypted = AES256_decrypt.decrypt(encrypted, password)
print(bytes.decode(decrypted))