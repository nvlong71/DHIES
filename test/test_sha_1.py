import hashlib
import time
import psutil
import os

def hash_sha1(message):
    sha1 = hashlib.sha1()
    sha1.update(message)
    return sha1.hexdigest()
def hash_sha256(message):
    sha256 = hashlib.sha256()
    sha256.update(message)
    return sha256.hexdigest()

def hash_sha512(message):
    sha512 = hashlib.sha512()
    sha512.update(message)
    return sha512.hexdigest()
with open('..\\data\message','r') as file:
    message = file.read()
message = message.encode()

# Bắt đầu đo lường tài nguyên
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss
start_cpu = process.cpu_percent(interval=None)
start_time = time.time()

# Thực hiện băm SHA-1 nhiều lần để tính thời gian trung bình
hash_result = hash_sha1(message)

# Kết thúc đo lường tài nguyên

end_time = time.time()
end_cpu = process.cpu_percent(interval=None)
end_memory = process.memory_info().rss

avg_time = (end_time - start_time)

print(f"hash result: {hash_result}")
print(f'Average time taken: {avg_time} seconds')
print(f'CPU usage: {end_cpu - start_cpu}%')
print(f'Memory usage: {end_memory - start_memory} bytes')


