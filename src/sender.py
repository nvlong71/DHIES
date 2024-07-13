from AES import encrypt_aes_cbc
import config
import util

if __name__ == '__main__':
    with open(f"{config.ROOT_FOLDER}\\data\plaintext", 'r', encoding='utf8') as file:
        plaintext = file.read()
    keys = util.gen_key(size_key_sym=config.SIZE_KEY_SYM, size_iv=config.SIZE_IV)
    sk = keys['sk']
    iv = keys['iv']
    ciphertext = encrypt_aes_cbc(plaintext=plaintext, key=sk, iv=iv)