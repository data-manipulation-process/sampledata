import os

fRootPath = "/Users/developer1/workspace/sampledata/class-1"
fFolder = "customer"
fFileName = "customer.txt"


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        print("New folder created")
