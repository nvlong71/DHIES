import os
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, hmac
import config


def create_tag(data: bytes, mac_key: bytes):
    hash_func = hashes.SHA256()
    h = hmac.HMAC(mac_key, hash_func)
    h.update(data)
    mac_tag = h.finalize()
    # with open(f'{config.ROOT_FOLDER}\\storage\\tag', 'wb') as tag_file:
    #     tag_file.write(mac_tag)
    return mac_tag


def validate_tag(data: bytes, mac_key: bytes, tag: bytes):
    hash_func = hashes.SHA256()
    h = hmac.HMAC(key=mac_key, algorithm=hash_func)
    h.update(data)
    try:
        h.verify(tag)
        return True
    except InvalidSignature:
        return False


if __name__ == '__main__':
    key = b'+\x16r\xdd@\xb9u\\\x9b\xc0\xea!(>\x04x\xf3\xdf}\xb5\xaf\x1egHM\xb1\x8b\xf3\xb5=\r\xb4'
    data = b'\xf8\xe2\xb6U&\xccf\xc6\xdd\xa0\x1e\xe5\x07P\x9b\xe9\xbe\xd5W3\xc4#s\xb0\xe4~\xff\x90\x15h\x8d)\x07\xfdW\xd2!\x1aP\xd7#\xbb\xcfj\x95\xbc\xaa\xadHn\xe4\x1a\xf2\x7f\xfd\xec\x1e\x02[\xc8\x84\xa6O\xd5\xcat\xa9\xe2&\xb7\x93\x95\xc5"}\xb9\xe7\x8e\xe5\x14z\x8cs\x97\xb2\x9eFi\xc0\x1fh\xf5d\x17\xb6b\x90\x89d\x9f\x80\xed\\\xfb\xe3\xaf\x0e\xa0K\x15\xa0\x8d\xab\xcfUy\xbc\xd0E\xac\xed\xdf\xf4I!NH\xc3\xb5)\x01{\x0e`\x1dB\xe6rZY6\xee\x89\xb7\xa1G\x99\xe2!\x1f\x1d\x9a\x05\x9e|\xa8*v\xedj\x1e\xc4\x81\x11\xdeN\xe2\xe8\xbf)\xb9\'U\xa3\x94\x0b\xd8]3\xf8xmi\xac\xf8\x84\xb1\x9bmi|\xbb\xe3\xa1 h\xc6\x19\xe2\x01\x8cS\xa28\xd71u\xc8\xcb\x1f\x82f\x89\x87\x1fX\xd0\xce$\xf61\xf0n\x19_\xa8\xa4C\xb5\x99g\xe7\xa2[,Db\x89\xaf\xc5\xf3,Ez\x9ce\x0b\xb9g\'\x06\xe6B\x881\x8c4e\xff6\xcb^\x99\xd1rE\xb2\x01\xe0\x8e\xf6\xbe\xbc\xe8a\x13+\xb89\xbb>\xd1\xf7\x82\xe9\x000\xd0\x8b\xf0\x1dk>\x9b\xacX\xb9\xab\x8f\x0b{\x10\xc6[\x05\x8e\xea$F\x8f\'\xb9\xf2\x8d\x8f2\xb1\x9f\xa8dH0\xfd\xaf\\\xa7\xe5TC\xed|-b k\xf2\xecn?\x08\xf6\xc8Y#`5\xd3\xb9\x03.\xb2C\r)\xebK\x9bR\xf8\x89\x81w\xdc\x9c\xdc\x80\xc2\xcfg\x87\x1a\xa2\x8af\xe7\xb4I\xdeEE\xff\x88_\xe4\x8aW\xbe\xbbq\x8a\x8a[\xe4\x99\xbe<\xfeF\xe6y\xda\xb9\x9d\x03K\xe7H\x91OH\xb6z\xa7\xcc\x05\x84'
    tag = b'`\xfe\xfco>\x8b}e\x0f\x0f\xb9\xc3\xb2\x10\xae\xbe\xcf\x1e\x96YfRR\xa5\x80\xec\x9c&\xd6\xa7\x1e3'



