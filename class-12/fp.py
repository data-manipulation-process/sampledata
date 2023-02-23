
import os

dirpath = "/Users/developer1/workspace/sampledata"


# text = input("Please enter text: " )
#
# print(text)

search_string = 'test'

import os

import glob

def search_string(directory, search_string,extension):
    for file in glob.glob(f'{directory}/**/*.{extension}'):
        print(file)
        with open(file, "r") as f:
            content = f.read()
            if search_string in content:
                print(f"Found '{search_string}' in {file}")
                print(content.index(search_string))

search_string(dirpath, 'index', 'txt')

