# main.py
# Python implementation of the MSc File Encryption Utility
# Provides a command-line interface for AES-GCM encryption and decryption.
# Developed as part of the MSc Artificial Intelligence (Launch into Computing) module.

import argparse as ap
from getpass import getpass
from crypto_functions import encrypt_file, decrypt_file
from cryptography.exceptions import InvalidTag
from pathlib import Path

# Define path to the local data directory
DATA_FOLDER = Path(__file__).resolve().parents[1] / "data"

# Set up command-line argument parser
parser = ap.ArgumentParser(
    prog="encryptor",
    description="Encrypt / Decrypt files",
    epilog="Example:\n  encryptor -a encrypt -s sample.txt -d sample.enc",
    formatter_class=ap.RawDescriptionHelpFormatter,
)

# Define CLI arguments for action, source file, and destination file
parser.add_argument(
    "-a",
    "--action",
    help="Select action to perform, either 'encrypt' or 'decrypt'",
    choices=["encrypt", "decrypt"],
    required=True,
)
parser.add_argument("-s", "--src", help="Select source file", required=True)
parser.add_argument("-d", "--dest", help="Select destination file", required=True)
args = parser.parse_args()


def main():
    """Main entry point for the encryption/decryption utility."""
    action = args.action
    src_file = args.src
    dest_file = args.dest

    # Display basic operation summary
    print(
        f"\nAction: {action}\nSource File: {src_file}\nDestination file: {dest_file}\n"
    )
    # Prompt user for password (hidden input)
    password = getpass(f"Please enter password to {action} {src_file}: ")
    # Perform file encryption or decryption
    try:
        if action == "encrypt":
            encrypt_file(
                src=DATA_FOLDER / src_file,
                dest=DATA_FOLDER / dest_file,
                password=password,
            )
            print(f"{src_file} successfuly encrypted to {dest_file}\n")
        elif action == "decrypt":
            decrypt_file(
                src=DATA_FOLDER / src_file,
                dest=DATA_FOLDER / dest_file,
                password=password,
            )
            print(f"{src_file} successfuly decrypted to {dest_file}\n")
        else:
            raise Exception
    # Handle common runtime errors gracefully
    except ValueError:
        print("Error: incorrect password")
    except PermissionError:
        print(f"Error: insufficient permissions for file")
    except FileNotFoundError:
        print(f"Error: file not found")
    except InvalidTag:
        print("Error: wrong password or corrupted file.")
    except Exception as e:
        print(f"Error: an unknown error occurred:\n {e}")


# Execute only when run directly
if __name__ == "__main__":
    main()
