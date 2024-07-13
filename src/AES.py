import os
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives import padding
import util
import config
import logging


def encrypt_aes_cbc(plaintext: str, key: bytes, iv: bytes):
    print("Encrypt")
    plaintext = plaintext.encode('utf-8')
    aes_cbc_cipher = Cipher(AES128(key), CBC(iv))
    padder = padding.PKCS7(AES128.block_size).padder()
    plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = aes_cbc_cipher.encryptor().update(plaintext)
    return ciphertext


def decrypt_aes_cbc(ciphertext: bytes, key: bytes, iv: bytes):
    print(f"Decrypt")
    aes_cbc_cipher = Cipher(AES128(key), CBC(iv))
    unpadder = padding.PKCS7(AES128.block_size).unpadder()

    plaintext = aes_cbc_cipher.decryptor().update(data=ciphertext)
    plaintext = unpadder.update(plaintext) + unpadder.finalize()
    return plaintext.decode()


if __name__ == "__main__":
    util.make_folder()
    plaintext = 'Demo encrypt AES128 nvlong nvlong nvlong'

    keys = util.gen_key(size_key_sym=config.SIZE_KEY_SYM, size_iv=config.SIZE_IV)
    sk = keys['sk']
    iv = keys['iv']
    ciphertext = encrypt_aes_cbc(plaintext=plaintext, key=sk, iv=iv)

    plaintext = decrypt_aes_cbc(ciphertext=ciphertext,key=sk,iv=iv)


    # print(ciphertext)
    # print(plaintext)