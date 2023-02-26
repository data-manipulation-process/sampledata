import os
import re

import numpy as np
import pandas as pd

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)

print(fPath)

# with open(fPath, 'r') as reader:
#     line = reader.readline()
#     while line != '':
#         print(line, end='')
#         line = reader.readline()

# with open(fPath, 'r') as reader:
#     for line in reader.readlines():
#         print(line, end='')

# with open(fPath, 'r') as reader:
#     for line in reader:
#         print(line, end='')

with open(fPath, 'r') as reader:
    line1 = reader.readlines()

with open(fPath, 'w') as writer:
    for line in reversed(line1):
        if not line.isspace():
            writer.write(line)
            print(line, end='')

# with open(fPath, 'r') as reader:
#     for line in reader:
#         if not line.isspace():
#             print(line, end='')

# Add n blank rows
