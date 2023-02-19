import os

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)

with open(fPath, 'r') as reader:
    print(reader.read())