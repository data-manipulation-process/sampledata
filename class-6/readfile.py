import os

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
        writer.write(line)