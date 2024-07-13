from AES import decrypt_aes_cbc
import config



if __name__ == '__main__':
    with open(f'{config.ROOT_FOLDER}\\data\sk', 'rb') as sk, open(f'{config.ROOT_FOLDER}\\data\\iv','rb') as iv, open(
            f'{config.ROOT_FOLDER}\\data\\ciphertext','rb') as ciphertext:
        sk = sk.read()
        iv = iv.read()
        ciphertext = ciphertext.read()

        plaintext = decrypt_aes_cbc(ciphertext=ciphertext,key=sk,iv=iv)
        print(plaintext)