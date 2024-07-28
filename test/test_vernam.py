import time
import psutil
import os
import numpy as np
def vernam_encrypt(key, message):
    key_repeated = np.tile(np.frombuffer(key, dtype=np.uint8), len(message) // len(key) + 1)[:len(message)]
    message_array = np.frombuffer(message, dtype=np.uint8)
    encrypted_array = np.bitwise_xor(message_array, key_repeated)
    return encrypted_array.tobytes()

with open('..\\data\\message','r') as file:
    message = file.read()

message = message.encode()
key = os.urandom(len(message))


process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss
start_cpu = process.cpu_percent(interval=None)
start_time = time.time()


encrypted_message = vernam_encrypt(key, message)


end_time = time.time()
end_cpu = process.cpu_percent(interval=None)
end_memory = process.memory_info().rss

avg_time = (end_time - start_time)
print(f'Average time taken: {avg_time} seconds')
print(f'CPU usage: {end_cpu - start_cpu}%')
print(f'Memory usage: {end_memory - start_memory} bytes')
