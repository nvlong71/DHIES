import time
import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'src'))
print(os.path.dirname(os.path.dirname(__file__)))
import sender
import receiver

run_time = []
for i in range(10):
    print(f'run {i+1} time')
    start_time = time.time()
    # sender.encrypt_dhies(
    # pk_path='storage/sender/ephemeral_pk_of_receiver',
    # m_path='storage/sender/message',
    # sk_path='storage/sender/sk'
    # )
    receiver.decrypt_dhies(em_path='storage/receiver/EM',
                           sk_path='storage/receiver/sk'
                           )
    end_time = time.time()
    execution_time = end_time - start_time
    run_time.append(execution_time)
    print(execution_time)

avg_time = sum(run_time) / len(run_time)
print(f'time excution average : {avg_time}')



    