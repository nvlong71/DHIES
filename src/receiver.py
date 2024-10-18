from AES import decrypt_aes_cbc
from HMAC import validate_tag
import config
import util
from util import modular
import random as rd
import argparse
import config
def gen_key():
    print('<---- gen pk and sk ---->')
    p = config.p
    g = config.g
    q = config.q
    v = rd.randint(1, q-1)
    pk = modular(g, v, p)D
    with (open(f'{config.ROOT_FOLDER}\\storage\\pk', 'w') as pk_file,
          open(f'{config.ROOT_FOLDER}\\storage\\sk', 'w') as sk_file):
        pk_file.write(str(pk))
        sk_file.write(str(v))
    return {
        "pk": modular(g, v, p),
        "sk": v
    }
def decrypt_dhies(em_path: str, sk_path: str):
    with open(em_path, 'r') as file_em, open(sk_path, 'r') as file_sk:
        em = file_em.read()
        sk = file_sk.read()
    extract_info = em.split('__')
    U = int(extract_info[0])
    enc_message = eval(extract_info[1])
    tag = eval(extract_info[2])

    sk = int(sk)
    p = config.p
    x = util.modular(U, sk, p)
    temp_hash = util.get_hash(str(x))
    keys = util.extract_key(temp_hash)
    enc_key = keys['enc_key']
    mac_key = keys['mac_key']
    print('<---- Decrypt ---->')
    iv = keys['iv']
    if not validate_tag(data=enc_message, mac_key=mac_key, tag=tag):
        print('BAD')
        return 'BAD'
    m = decrypt_aes_cbc(enc_message, enc_key, iv)
    print(m)
    return m


    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Params for receiver')
    parser.add_argument('--action', help='"gen_key" or "decrypt"')
    parser.add_argument('--em', help='path to encrypt message from sender')
    parser.add_argument('--sk', help='path to secret key')
    args = parser.parse_args()
    action = args.action
    if action == 'gen_key':
        gen_key()
    elif action == 'decrypt':
        em = args.em
        sk = args.sk
        decrypt_dhies(em_path=em, sk_path=sk)
