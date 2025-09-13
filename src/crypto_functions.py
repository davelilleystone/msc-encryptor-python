def derive_key(password: str, salt: bytes) -> bytes:
    return


def encrypt_file(src: str, dest: str, password: str) -> None:
    with open(src) as file:
        txt = file.read()
        print(txt)


def decrypt_file(src: str, dest: str, password: str) -> None:
    print("decrypt_file")
    return
