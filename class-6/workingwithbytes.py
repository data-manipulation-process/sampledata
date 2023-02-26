import os

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)

print(fPath)

# with open(fPath, 'r') as reader:
#     line1 = reader.readlines()
#
# with open(fPath, 'w') as writer:
#     for line in reversed(line1):
#         if not line.isspace():
#             writer.write(line)
#             print(line, end='')
with open(fPath, 'rb') as reader:
    print(reader.read(10))
    print(reader.read(3))
    print(reader.read(2))
