import os

from common import common
from common.common import fRootPath, fFolder, fFileName, create_dir

pFolder = os.path.join(fRootPath, fFolder)
pFile = os.path.join(pFolder, fFileName)

print(pFolder, "\n", pFile)

create_dir(pFolder)

with open(pFile, 'a+') as f:
    content = "I can eat any spam file\n"
    f.write(content)
    f.close()
    print("New content written in the file")

with open(pFile, 'r') as f:
    for i, lines in enumerate(f):
        print(f'Line: {i+1}, content: {lines}'.strip())