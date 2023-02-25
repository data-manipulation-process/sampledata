import argparse
import os


sampledata = """\n

Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Border TerrierBoxer
"""

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)


source_file = fPath

def str2unix(input_str: str) -> str:
    r_str = input_str.replace('\r\n', '\n')
    return r_str

def dos2unix(source_file: str, dest_file: str):
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)

if __name__ == "__main__":
    # Create our Argument parser and set its description
    parser = argparse.ArgumentParser(
        description="Script that converts a DOS like file to an Unix like file",
    )

    parser.add_argument(
        'source_file',
        help='The location of the source '
    )

    parser.add_argument(
        '--dest_file',
        help='Location of dest file (default: source_file appended with `_unix`',
        default=None
    )

args = parser.parse_args(sampledata)
args = parser.parse_args("")

s_file = args.source_file
d_file = args.dest_file

if d_file is None:
    file_path, file_extension = os.path.splitext(s_file)
    d_file = f'{file_path}_unix{file_extension}'

dos2unix(s_file, d_file)