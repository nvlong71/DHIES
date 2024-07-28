from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
import hashlib
import time
import psutil
import os

def compute_hmac(key, message):
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(message)
    return h.finalize()

def test_hmac():
    key = os.urandom(16)
    with open('..\\data\\message', 'r') as file:
        message = file.read()
    message = message.encode()

    # Bắt đầu đo lường tài nguyên
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss
    start_cpu = process.cpu_percent(interval=None)
    start_time = time.time()

    # Thực hiện HMAC nhiều lần để tính thời gian trung bình
    hmac_result = compute_hmac(key, message)

    # Kết thúc đo lường tài nguyên
    end_time = time.time()
    end_cpu = process.cpu_percent(interval=None)
    end_memory = process.memory_info().rss

    avg_time = (end_time - start_time)

    print(f'HMAC: {hmac_result}')
    print(f'Average time taken: {avg_time} seconds')
    print(f'CPU usage: {(end_cpu - start_cpu)}%')
    print(f'Memory usage: {end_memory - start_memory} bytes')



if __name__ == '__main__':
    test_hmac()
    
