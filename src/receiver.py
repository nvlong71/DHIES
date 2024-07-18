from AES import decrypt_aes_cbc
from HMAC import validate_tag
import config
import util
from util import modular
import random as rd

def gen_key():
    with open(f'{config.ROOT_FOLDER}\\storage\\p', 'r') as file:
        p = int(file.read())
    with open(f'{config.ROOT_FOLDER}\\storage\\g', 'r') as file:
        g = int(file.read())
    v = rd.randint(1, p)
    pk = modular(g, v, p)
    with (open(f'{config.ROOT_FOLDER}\\storage\\pk', 'w') as pk_file,
          open(f'{config.ROOT_FOLDER}\\storage\\sk', 'w') as sk_file):
        pk_file.write(str(pk))
        sk_file.write(str(v))
    return {
        "pk": modular(g, v, p),
        "sk": v
    }
def decrypt_dhies(em: str, sk: str):
    pass

if __name__ == '__main__':
    # with open(f'{config.ROOT_FOLDER}\\data\sk', 'rb') as sk, open(f'{config.ROOT_FOLDER}\\data\\iv','rb') as iv, open(
    #         f'{config.ROOT_FOLDER}\\data\\ciphertext', 'rb') as ciphertext:
    #     sk = sk.read()
    #     iv = iv.read()
    #     ciphertext = ciphertext.read()
    #     plaintext = decrypt_aes_cbc(ciphertext=ciphertext,key=sk,iv=iv)
    #     print(plaintext)

    # with open(f'{config.ROOT_FOLDER}\\data\\mac_key','rb') as mac_key_file:
    #     key = mac_key_file.read()
    # with open(f'{config.ROOT_FOLDER}\\data\\plaintext','r',encoding='utf8') as file:
    #     plaintext = file.read()
    # with open(f'{config.ROOT_FOLDER}\\data\\tag','rb') as tag:
    #     mac_tag = tag.read()

    # verify = validate_tag(plaintext=plaintext, mac_key=key,tag=mac_tag)
    # print(verify)

    util.init()
    keys = gen_key()
    print(f'SK : {keys["sk"]}')
    print(f'PK : {keys["pk"]}')
