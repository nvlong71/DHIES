from AES import decrypt_aes_cbc
from HMAC import validate_tag
import config



if __name__ == '__main__':
    # with open(f'{config.ROOT_FOLDER}\\data\sk', 'rb') as sk, open(f'{config.ROOT_FOLDER}\\data\\iv','rb') as iv, open(
    #         f'{config.ROOT_FOLDER}\\data\\ciphertext', 'rb') as ciphertext:
    #     sk = sk.read()
    #     iv = iv.read()
    #     ciphertext = ciphertext.read()
    #
    #     plaintext = decrypt_aes_cbc(ciphertext=ciphertext,key=sk,iv=iv)
    #     print(plaintext)

    key = b'+\x16r\xdd@\xb9u\\\x9b\xc0\xea!(>\x04x\xf3\xdf}\xb5\xaf\x1egHM\xb1\x8b\xf3\xb5=\r\xb4'
    with open(f'{config.ROOT_FOLDER}\\data\\plaintext','r',encoding='utf8') as file:
        plaintext = file.read()
    # create_tag(plaintext, key)
    with open(f'{config.ROOT_FOLDER}\\data\\tag','rb') as tag:
        mac_tag = tag.read()

    verify = validate_tag(plaintext=plaintext, mac_key=key,tag=mac_tag)
    print(verify)
