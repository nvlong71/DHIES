import os

from AES import encrypt_aes_cbc
from HMAC import create_tag
import config
import util
from util import modular
import random as rd
import argparse

def gen_iv():
    return os.getrandom(16)

def encrypt_dhies(pk_path: str, m_path: str):
    p = config.p
    g = config.g
    q = config.q
    u = rd.randint(1, q-1)
    with open(pk_path,'r') as pk_file, open(m_path,'r') as m_file:
        M = m_file.read()
        pk = pk_file.read()
    message = M
    pk = int(pk)
    # tinh khóa bí mật chung x
    x = modular(pk, u, p)
    # Tính khóa bí mật tạm thời U
    U = modular(g, u, p)
    temp_hash = util.get_hash(str(x))
    key_extracted = util.extract_key(temp_hash)
    mac_key = key_extracted['mac_key']
    enc_key = key_extracted['enc_key']

    # iv = key_extracted['iv']
    iv = gen_iv()
    enc_message = encrypt_aes_cbc(plaintext=message, key=enc_key, iv=iv)
    tag = create_tag(data=enc_message, mac_key=mac_key)
    EM = '_$_$'.join([str(U), str(enc_message), str(tag),str(iv)])
    # EM = f'''{str(U)}__{str(enc_message)}__{str(tag)}__{str(iv)}'''
    print('<---- Encrypt Message ---->\n' + EM)
    path_em = os.path.join(config.ROOT_FOLDER,'storage/EM')
    with open(path_em, 'w') as em_file:
        em_file.write(EM)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Param for sender')
    parser.add_argument('--m', help='path to plaintext to encrypt')
    parser.add_argument('--pk', help='path to ephermal public key')
    args = parser.parse_args()
    em = args.m
    pk = args.pk
    encrypt_dhies(m_path=em, pk_path=pk)









