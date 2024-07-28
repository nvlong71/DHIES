import hmac
import hashlib
import time
import psutil
import os

def compute_hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

key = b'secret_key'
message = b'This is a message'

# Bắt đầu đo lường tài nguyên
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss
start_cpu = process.cpu_percent(interval=None)
start_time = time.time()

# Thực hiện HMAC nhiều lần để tính thời gian trung bình
num_iterations = 10000
for _ in range(num_iterations):
    hmac_result = compute_hmac(key, message)

# Kết thúc đo lường tài nguyên
end_time = time.time()
end_cpu = process.cpu_percent(interval=None)
end_memory = process.memory_info().rss

avg_time = (end_time - start_time) / num_iterations

print(f'HMAC: {hmac_result}')
print(f'Average time taken: {avg_time} seconds')
print(f'CPU usage: {(end_cpu - start_cpu) / num_iterations}%')
print(f'Memory usage: {end_memory - start_memory} bytes')
