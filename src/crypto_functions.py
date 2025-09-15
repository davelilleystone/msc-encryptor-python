import secrets
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    return kdf.derive(password.encode())


def encrypt_bytes(data: bytes, password: str) -> bytes:
    salt = secrets.token_bytes(16)
    nonce = secrets.token_bytes(12)
    derived_key = derive_key(password, salt)
    aesgcm = AESGCM(derived_key)
    ct_plus_tag = aesgcm.encrypt(nonce=nonce, data=data, associated_data=None)
    return salt + nonce + ct_plus_tag


def decrypt_bytes(data: bytes, password: str) -> bytes:
    salt = data[:16]
    nonce = data[16:28]
    ct_plus_tag = data[28:]
    derived_key = derive_key(password=password, salt=salt)
    aesgcm = AESGCM(derived_key)
    decrypted_ct = aesgcm.decrypt(nonce=nonce, data=ct_plus_tag, associated_data=None)
    return decrypted_ct


def encrypt_file(src: str, dest: str, password: str) -> None:
    with open(src, "rb") as file:
        txt = file.read()
    payload = encrypt_bytes(txt, password)
    with open(dest, "wb") as file:
        file.write(payload)


def decrypt_file(src: str, dest: str, password: str) -> None:
    with open(src, "rb") as file:
        data = file.read()
    plaintext = decrypt_bytes(data=data, password=password)
    with open(dest, "wb") as file:
        file.write(plaintext)
    return
