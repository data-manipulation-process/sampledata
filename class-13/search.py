import glob
import os
import re

dirpath = '/Users/developer1/workspace/sampledata'


def search_string5(dicrectory, search_string, extension):
    for file in glob.glob(f'{dicrectory}/**/*.{extension}'):
        with open(file, 'r') as f:
            content = f.readlines()
            for line, name in enumerate(content):
                if re.search(search_string, name):
                    print(file)
                    print('Line Number:', line, name, end='')
                    print(f'index', name.index(search_string))
                    print()


search_string5(dirpath, 'search_string5', 'py')
