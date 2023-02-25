import os
import glob

rootdir = '/Users/developer1/workspace/sampledata'
#


def search_string(root, word):
    for path_list in glob.glob(f'{rootdir}/*/*', recursive=True):
        print(path_list)
        with open(path_list, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                if line.find(word) != -1:
                    print(word, 'string exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)

search_string(rootdir, 'test')

