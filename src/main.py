import argparse as ap
from getpass import getpass
from crypto_functions import encrypt_file, decrypt_file

parser = ap.ArgumentParser(
    prog="encryptor",
    description="Encrypt / Decrypt files",
    epilog="Example:\n  encryptor -a encrypt -s data/sample.txt -d data/sample.enc",
    formatter_class=ap.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-a",
    "--action",
    help="Select action to perform - 'encrypt' or 'decrypt'",
    choices=["encrypt", "decrypt"],
    required=True,
)
parser.add_argument("-s", "--src", help="Select source file", required=True)
parser.add_argument("-d", "--dest", help="Select destination file", required=True)
args = parser.parse_args()


def main():

    action = args.action
    src_file = args.src
    dest_file = args.dest

    print(
        f"\nAction: {action}\nSource File: {src_file}\nDestination file: {dest_file}\n"
    )

    password = getpass(f"Please enter password to {action} {src_file}: ")
    print(password)  # TODO: remove after testing

    try:
        if action == "encrypt":
            encrypt_file(src=src_file, dest=dest_file, password=password)
        elif action == "decrypt":
            decrypt_file(src=src_file, dest=dest_file, password=password)
        else:
            raise Exception
    except ValueError:
        print("Error: incorrect password")
    except PermissionError:
        print(f"Error: insufficient permissions for file")
    except FileNotFoundError:
        print(f"Error: file not found")
    except Exception:
        print(f"Error: an unknown error occurred")


if __name__ == "__main__":
    main()
