import time
import subprocess

# Bắt đầu đo thời gian
start_time = time.time()

# Chạy lệnh
# subprocess.run(["python", "src/sender.py", "--m", "data/big.txt", "--pk", "storage/pk"])
subprocess.run(["python", "src/receiver.py", "--em", "storage/EM", "--sk", "storage/sk", "--action", "decrypt"])
# Kết thúc đo thời gian
end_time = time.time()
execution_time = end_time - start_time

print(f"Thời gian chạy: {execution_time} giây")
