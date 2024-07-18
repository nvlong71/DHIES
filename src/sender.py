import os

from AES import encrypt_aes_cbc
from HMAC import create_tag
import config
import util
from util import modular
import random as rd


def encrypt_dhies(pk: str, M: str):
    param = util.load_param()
    p = param['p']
    g = param['g']
    u = rd.randint(1, p)
    message = M
    pk = int(pk)
    # tinh khóa bí mật chung x
    x = modular(pk, u, p)
    # Tính khóa bí mật tạm thời U
    U = modular(g, u, p)
    print(f"Khóa bí mật chung X : {x}")
    print(f"Khóa bí mật tạm thời U : {U}")
    temp_hash = util.get_hash(str(x))
    key_extracted = util.extract_key(temp_hash)
    mac_key = bytes.fromhex(key_extracted['mac_key'])
    enc_key = bytes.fromhex(key_extracted['enc_key'])
    iv = bytes.fromhex(key_extracted['iv'])
    print(f"MAC KEY : {len(mac_key)} bytes")
    print(f"ENC KEY : {len(enc_key)} bytes")
    print(f"IV      : {len(iv)} bytes")

    # print(f"MAC KEY : {mac_key} bytes")
    # print(f"ENC KEY : {str(enc_key)} bytes")
    # print(f"IV :      {iv} bytes")

    enc_message = encrypt_aes_cbc(plaintext=message, key=enc_key, iv=iv)
    tag = create_tag(plaintext=message,mac_key=mac_key)

    print(f'enc_message : {enc_message}')
    print(f'tag: {tag}')

    EM = '__'.join([str(U), str(enc_message), str(tag)])
    with open(f'{config.ROOT_FOLDER}\\storage\\EM', 'w') as em_file:
        em_file.write(EM)
    print(EM)


if __name__ == '__main__':
    

    encrypt()







