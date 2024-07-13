import os
from cryptography.exceptions import  InvalidSignature
from cryptography.hazmat.primitives import hashes, hmac
import config

def create_tag(plaintext: str, mac_key: bytes):
    hash_func = hashes.SHA256()
    h = hmac.HMAC(mac_key, hash_func)
    plaintext = plaintext.encode('utf-8')
    h.update(plaintext)
    mac_tag = h.finalize()
    with open(f'{config.ROOT_FOLDER}\\data\\tag','wb') as tag_file:
        tag_file.write(mac_tag)
    return mac_tag
def validate_tag(plaintext: str, mac_key: bytes, tag: bytes):
    plaintext = plaintext.encode('utf8')
    hash_func = hashes.SHA256()
    h = hmac.HMAC(key=mac_key, algorithm=hash_func)
    h.update(plaintext)
    try:
        h.verify(tag)
        return True
    except InvalidSignature:
        return False




if __name__ == '__main__':
    key = b'+\x16r\xdd@\xb9u\\\x9b\xc0\xea!(>\x04x\xf3\xdf}\xb5\xaf\x1egHM\xb1\x8b\xf3\xb5=\r\xb4'
    with open(f'{config.ROOT_FOLDER}\\data\\plaintext','r',encoding='utf8') as file:
        plaintext = file.read()
    # create_tag(plaintext, key)
    with open(f'{config.ROOT_FOLDER}\\data\\tag','rb') as tag:
        mac_tag = tag.read()

    verify = validate_tag(plaintext=plaintext, mac_key=key,tag=mac_tag)
    print(verify)

