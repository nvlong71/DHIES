import os

from AES import encrypt_aes_cbc
from HMAC import create_tag
import config
import util

if __name__ == '__main__':
    # with open(f"{config.ROOT_FOLDER}\\data\plaintext", 'r', encoding='utf8') as file:
    #     plaintext = file.read()
    # keys = util.gen_key(size_key_sym=config.SIZE_KEY_SYM, size_iv=config.SIZE_IV)
    # sk = keys['sk']
    # iv = keys['iv']
    # ciphertext = encrypt_aes_cbc(plaintext=plaintext, key=sk, iv=iv)


    key = os.urandom(config.MAC_KEY)
    with open(f'{config.ROOT_FOLDER}\\data\\mac_key','wb') as file:
        file.write(key)
    with open(f'{config.ROOT_FOLDER}\\data\\plaintext', 'r', encoding='utf8') as file:
        plaintext = file.read()
    create_tag(plaintext, key)