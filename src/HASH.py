import config

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend



# Đường dẫn tới tệp tin cần băm
file_path = 'path/to/your/file'

# Tạo đối tượng băm SHA-256
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

# Đọc tệp tin và cập nhật đối tượng băm
with open(file_path, 'rb') as f:
    while chunk := f.read(8192):
        digest.update(chunk)

# Lấy giá trị băm
hash_bytes = digest.finalize()

# Chuyển đổi giá trị băm thành chuỗi hex
hash_hex = hash_bytes.hex()

print(f"SHA-256 hash of the file: {hash_hex}")
