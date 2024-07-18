import os

from AES import encrypt_aes_cbc
from HMAC import create_tag
import config
import util
from util import modular
import random as rd


def encrypt():
    pass


if __name__ == '__main__':
    
    
    # ----------> Encrypt
    # with open(f"{config.ROOT_FOLDER}\\data\plaintext", 'r', encoding='utf8') as file:
    #     plaintext = file.read()
    # keys = util.gen_key(size_key_sym=config.SIZE_KEY_SYM, size_iv=config.SIZE_IV)
    # sk = keys['sk']
    # iv = keys['iv']
    # ciphertext = encrypt_aes_cbc(plaintext=plaintext, key=sk, iv=iv)

    # -----------> create MAC
    # key = os.urandom(config.MAC_KEY)
    # with open(f'{config.ROOT_FOLDER}\\data\\mac_key','wb') as file:
    #     file.write(key)
    # with open(f'{config.ROOT_FOLDER}\\data\\plaintext', 'r', encoding='utf8') as file:
    #     plaintext = file.read()
    # create_tag(plaintext, key)

    param = util.load_param()
    p = param['p']
    g = param['g']
    u = rd.randint(1, p)
    with open(f'{config.ROOT_FOLDER}\\data\\message', 'r', encoding='utf8') as message_file, open(f'{config.ROOT_FOLDER}\\data\\pk') as pk_file:
        message = message_file.read()
        pk = int(pk_file.read())


    print("Alice Encrypt")
    # tinh khóa bí mật chung x
    x = modular(pk, u, p)
    # Tính khóa bí mật tạm thời U
    U = modular(g, u, p)
    print(f"Khóa bí mật chung X : {x}")
    print(f"Khóa bí mật tạm thời U : {U}")
    temp_hash = util.get_hash(str(x))
    key_extracted = util.extract_key(temp_hash)
    mac_key = key_extracted['mac_key']
    enc_key = key_extracted['enc_key']
    print(f"MAC KEY : {mac_key}")
    print(f"ENC KEY : {enc_key}")
    # print(util.extract_key(temp_hash))
    # print(bytes.fromhex(temp_hash))






