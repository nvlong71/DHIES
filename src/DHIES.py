import util
import sender
import receiver
import config

if __name__ == '__main__':
    util.init()

    print("Bob gen key")
    receiver.gen_key()

    print("Alice Encrypt Message")
    with (open(f'{config.ROOT_FOLDER}\\storage\\pk', 'r') as pk_file,
          open(f'{config.ROOT_FOLDER}\\data\\message', 'r') as message_file):
        pk = pk_file.read()
        message = message_file.read()
    sender.encrypt_dhies(pk=pk, M=message)


    print('Bob Decrypt Ciphertext')
    with open(f'{config.ROOT_FOLDER}\\storage\\EM', 'r') as em_file, open(f'{config.ROOT_FOLDER}\\storage\\sk', 'r') as sk_file:
        em = em_file.read()
        sk = sk_file.read()
    receiver.decrypt_dhies(em=em, sk=sk)
