


file_name = 'myfile.txt'


def search_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)

def search_file_2(file_name, search_string):
    with open(file_name, 'r') as file:
        for i, name in enumerate(file):
            i += 1
            print(f'Line Number {i}:', name,end='')

# search_file(file_name)
# search_file_2(file_name,'test')

def search_file_3(file_name, search_string):
    with open(file_name, 'r') as files:
        file= files.readlines()
        for name in file:
            if name.find(search_string) != -1:
                print(search_string, 'string exists in file')
                print('Line Number: ', file.index(name)+1)
                print('File Content: ', name, end='')
                print()


search_file_3(file_name,'python')

"""
for loop 
if find !=1 
index 

"""