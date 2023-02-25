import os


filepath = 'myfile2.txt'
filedir = '/Users/developer1/workspace/sampledata/class-11'

flag = os.path.isfile(filepath)
if flag:
    print(f'The file {filepath} exists')
else:
    print(f'the file {filepath} does not eixst')

print(os.path.isfile(filepath))
print(os.path.isdir(filedir))

from pathlib import Path

path = Path(filepath)
if path.is_file():
    print(f'the file {filepath} exists')
else:
    print(f'the file {filepath} does not exist')

