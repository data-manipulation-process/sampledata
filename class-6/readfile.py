import os

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)

print(fPath)

with open(fPath, 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        line = reader.readline()