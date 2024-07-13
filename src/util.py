import os
import random
import config
from pathlib import Path
def make_folder():
    Path(f'{config.ROOT_FOLDER}\\data').mkdir(exist_ok=True)
def gen_key(size_key_sym: int, size_iv: int):
    sk = os.urandom(size_key_sym//8)
    iv = os.urandom(size_key_sym//8)
    with open(f'{config.ROOT_FOLDER}\\data\\sk.bin','wb') as file:
        file.write(sk)
    with open(f'{config.ROOT_FOLDER}\\data\\iv.bin', 'wb') as file:
        file.write(iv)

    return {
        "sk": sk,
        "iv": iv
    }


if __name__ == "__main__":
    print(gen_key(128,128))

    with open(f'{config.ROOT_FOLDER}\\data\\sk', 'rb') as file:
        data = file.read()
        print(data)
    with open(f'{config.ROOT_FOLDER}\\data\\iv', 'rb') as file:
        data = file.read()
        print(data)
