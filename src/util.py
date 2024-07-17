import os
import random
import config
from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
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

def modular(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # Nếu exponent là lẻ
            result = (result * base) % modulus
        exponent = exponent >> 1  
        base = (base * base) % modulus
    return result

def init():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    p = parameters.parameter_numbers().p
    g = parameters.parameter_numbers().g
    print(p)
    print(g)
    with open(f'{config.ROOT_FOLDER}\\data\\p','w') as file:
        file.write(p)
    with open(f'{config.ROOT_FOLDER}\\data\\g','w') as file:
        file.write(g)
        
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

    s = modular(2,6,5)
    print(s)