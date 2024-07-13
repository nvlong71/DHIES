import os
import random
import config
from pathlib import Path
def make_folder():
    Path(f'{config.ROOT_FOLDER}\\data').mkdir(exist_ok=True)
def gen_key(size_key_sym: int, size_iv: int):
    sk = os.urandom(size_key_sym)
    iv = os.urandom(size_key_sym)
    with open(f'{config.ROOT_FOLDER}\\data\\sk.bin','wb') as file:
        file.write(sk)
    with open(f'{config.ROOT_FOLDER}\\data\\iv.bin', 'wb') as file:
        file.write(iv)

    return {
        "sk": sk,
        "iv": iv
    }


if __name__ == "__main__":
    print(gen_key(16,16))

    with open(f'{config.ROOT_FOLDER}\\data\\sk.bin', 'rb') as file:
        data = file.read()
        print(data)
    with open(f'{config.ROOT_FOLDER}\\data\\iv.bin', 'rb') as file:
        data = file.read()
        print(data)
