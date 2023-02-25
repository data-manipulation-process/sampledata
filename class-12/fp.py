import os
import re

dirpath = "/Users/developer1/workspace/sampledata"

import glob


def search_string(directory, search_string, extension):
    for file in glob.glob(f'{directory}/**/*.{extension}'):
        # print(file)
        with open(file, "r") as f:
            content = f.read()
            if search_string in content:
                print(f"Found '{search_string}' in {file}")
                print(content.index(search_string))


# search_string(dirpath, 'test', 'txt')


def search_string3(directory, search_string, extension):
    for file in glob.glob(f'{directory}/**/*.{extension}'):
        with open(file, 'r') as f:
            content = f.readlines()
            for i, line in enumerate(content):
                if re.search(search_string, line):
                    print(f"Found '{search_string}' in {file}")
                    print(f'Line number:{i + 1}; Content: {line}'.strip())
                    print()


# search_string3(dirpath, 'test', 'py')


def search_string4(directory, search_string, extension):
    for file in glob.glob(f'{directory}/**/*.{extension}'):
        # print(file)
        with open(file, 'r') as f:
            content = f.readlines()
            # print(content)
            for i, line in enumerate(content):
                # print(i, line)
                if re.search(search_string, line):
                    print(f"Found '{search_string}' in {file}")
                    print(f'Line number:{i + 1}; Content: {line}'.strip())
                    print()


# search_string4(dirpath, 'test', 'py')


"""
get only files need by - filter
read file
line number, read file
reg search - print line number with line content
"""


def search_string5(dicrectory, search_string, extension):
    for file in glob.glob(f'{dicrectory}/**/*.{extension}'):
        with open(file, 'r') as f:
            content = f.readlines()
            for line, name in enumerate(content):
                if re.search(search_string, name):
                    print(file)
                    print('Line Number:',line, name,end='')
                    print(f'index' , name.index(search_string))
                    print()

search_string5(dirpath, 'test', 'py')
