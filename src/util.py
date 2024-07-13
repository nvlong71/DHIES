import os
import random
import config
from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
def make_folder():
    Path(f'{config.ROOT_FOLDER}\\data').mkdir(exist_ok=True)
def gen_key(size_key_sym: int, size_iv: int):
    sk = os.urandom(size_key_sym//8)
    iv = os.urandom(size_key_sym//8)

    with open(f'{config.ROOT_FOLDER}\\data\\sk','wb') as file:
        file.write(sk)
    with open(f'{config.ROOT_FOLDER}\\data\\iv', 'wb') as file:
        file.write(iv)

    return {
        "sk": sk,
        "iv": iv
    }

def create_hash(data: str):
    data = data.encode('utf8')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    hash_bytes = digest.finalize()
    hash_hex = hash_bytes.hex()
    return hash_hex

if __name__ == "__main__":
    data = 'hello world'
    hash = create_hash(data)
    print(hash)
