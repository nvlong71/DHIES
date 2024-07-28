from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import time
import psutil
import os


def pad_message(message, block_size=16):
    padding_len = block_size - (len(message) % block_size)
    padding = bytes([padding_len] * padding_len)
    return message + padding

def aes_encrypt(key, iv, message):
    message = pad_message(message)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(message) + encryptor.finalize()

key = os.urandom(16)
iv = os.urandom(16)

with open('..\\data\\message','r') as file:
    message = file.read()
message = message.encode()


process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss
start_cpu = process.cpu_percent(interval=None)
start_time = time.time()
encrypted_message = aes_encrypt(key, iv, message)
end_time = time.time()
end_cpu = process.cpu_percent(interval=None)
end_memory = process.memory_info().rss

avg_time = (end_time - start_time)
print(f'Time taken: {avg_time} seconds')
print(f'CPU usage: {end_cpu - start_cpu}%')
print(f'Memory usage: {end_memory - start_memory} bytes')
