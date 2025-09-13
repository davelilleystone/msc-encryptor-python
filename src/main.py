import argparse as ap

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

    print(action, src_file, dest_file)


if __name__ == "__main__":
    main()
