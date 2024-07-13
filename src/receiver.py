from AES import decrypt_aes_cbc
from HMAC import validate_tag
import config



if __name__ == '__main__':
    # with open(f'{config.ROOT_FOLDER}\\data\sk', 'rb') as sk, open(f'{config.ROOT_FOLDER}\\data\\iv','rb') as iv, open(
    #         f'{config.ROOT_FOLDER}\\data\\ciphertext', 'rb') as ciphertext:
    #     sk = sk.read()
    #     iv = iv.read()
    #     ciphertext = ciphertext.read()
    #     plaintext = decrypt_aes_cbc(ciphertext=ciphertext,key=sk,iv=iv)
    #     print(plaintext)

    with open(f'{config.ROOT_FOLDER}\\data\\mac_key','rb') as mac_key_file:
        key = mac_key_file.read()
    with open(f'{config.ROOT_FOLDER}\\data\\plaintext','r',encoding='utf8') as file:
        plaintext = file.read()
    with open(f'{config.ROOT_FOLDER}\\data\\tag','rb') as tag:
        mac_tag = tag.read()

    verify = validate_tag(plaintext=plaintext, mac_key=key,tag=mac_tag)
    print(verify)
