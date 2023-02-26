import os
from Pngreader import PngReader

#
# imgName = "/Users/developer1/workspace/sampledata/class-6/img.png"
#
#

# with PngReader(imgName) as reader:
#      for l, t, d, c in reader:
#          print(f"{l:05}, {t}, {c}")

fDir = "/Users/developer1/workspace/sampledata/class-6"
fFile = "newslines.txt"

fPath = os.path.join(fDir, fFile)

with open(fPath, 'r') as reader:
    reader.read()

with open(fPath, 'a') as writer:
    print(writer.write('\n\nBeagle\n'))
