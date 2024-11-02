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

def gen_key():
    print('<---- sender ephemeral_pk and sk ---->')
    p = config.p
    g = config.g
    q = config.q
    v = rd.randint(1, q-1)
    pk = modular(g, v, p)
    path_sk = os.path.join(config.STORAGE_SENDER,'sk')
    
    with open(path_sk, 'w') as sk_file:
        sk_file.write(str(v))
    
    return {
        "pk": pk,  
        "sk": v
    }


def encrypt_dhies(pk_path: str, m_path: str):
    p = config.p
    g = config.g
    q = config.q
    # u = rd.randint(1, q-1)

    with open(pk_path,'r') as pk_file, \
            open(m_path,'r') as m_file , \
            open(os.path.join(f'{config.STORAGE_SENDER}/sk'), 'r') as sk_file:
        M = m_file.read()
        pk = pk_file.read()
        u = sk_file.read()
    message = M
    pk = int(pk)
    u = int(u)
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
    
    path_em = os.path.join(config.STORAGE_RECEIVER,'EM')
    with open(path_em, 'w') as em_file:
        em_file.write(EM)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Param for sender')
    parser.add_argument('--m', help='path to plaintext to encrypt')
    parser.add_argument('--pk', help='path to ephermal public key')
    parser.add_argument('--action', help='"gen_key" or "encrypt"')
    args = parser.parse_args()
    action = args.action
    if action == 'gen_key':
        util.make_folder()
        gen_key()
    else:
        em = args.m
        pk = args.pk
        encrypt_dhies(m_path=em, pk_path=pk)









