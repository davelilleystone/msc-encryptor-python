import secrets
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    return kdf.derive(password.encode())


def encrypt_file(src: str, dest: str, password: str) -> None:
    salt = secrets.token_bytes(16)
    derived_key = derive_key(password, salt)
    with open(src) as file:
        txt = file.read()
        print(txt)


def decrypt_file(src: str, dest: str, password: str) -> None:
    print("decrypt_file")
    return


password = "hello"
salt = secrets.token_bytes(16)

key = derive_key(password=password, salt=salt)

print(key)
