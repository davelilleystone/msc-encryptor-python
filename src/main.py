import argparse as ap
from getpass import getpass

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
    print(password)


if __name__ == "__main__":
    main()
