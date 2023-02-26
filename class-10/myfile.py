import os

file_name = 'myfile.txt'


def search_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)


def search_file_2(file_name, search_string):
    with open(file_name, 'r') as file:
        for i, name in enumerate(file):
            i += 1
            print(f'Line Number {i}:', name, end='')


# search_file(file_name)
# search_file_2(file_name,'test')

def search_file_3(file_name, search_string):
    with open(file_name, 'r') as files:
        file = files.readlines()
        for name in file:
            if name.find(search_string) != -1:
                print(search_string, 'string exists in file')
                print('Line Number: ', file.index(name) + 1)
                print('File Content: ', name, end='')
                print()


# search_file_3(file_name,'python')

"""
for loop 
if find !=1 
index 

"""


def search_file_4(file_name, search_name):
    with open(file_name, 'r') as files:
        file = files.readlines()
        print(file)
        for line in file:
            if line.find(search_name) != -1:
                print(search_name, ' :string exists in the file')
                print('Line Number: ', file.index())
                print(line)


# search_file_4(file_name, 'test')

words = ['test']

with open(file_name, 'r') as f:
    content = f.readlines()

for word in words:
    if word in content:
        print(word, 'string exist in a file')
        print(content)

for lines_content in content:
    if lines_content.find("python") != -1:
        print(lines_content, end='')
    if lines_content.find('test') != -1:
        print(lines_content, end='')

listoffils = os.listdir('/Users/developer1/workspace/sampledata/class-10')
print(listoffils)

"""
def - function
with - clause to read
for 
if 
find 
"""
