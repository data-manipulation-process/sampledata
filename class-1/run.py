import os

fRootPath = "/Users/developer1/workspace/sampledata/class-1"
fFolder = "customer"
fFileName = "customer.txt"

pFolder = os.path.join(fRootPath, fFolder)
pFile = os.path.join(pFolder, fFileName)

print(pFolder, "\n", pFile)

