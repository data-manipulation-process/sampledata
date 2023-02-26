file_name = 'myfile.txt'

print(file_name)


def print_file(file):
    with open(file) as file_con_raw:
        file_content = file_con_raw.read()
        print(file_content)


def print_file2(file, serch):
    with open(file) as file_con_raw:
        file_content = file_con_raw.readlines()
        for line in file_content:
            if line.find(serch) != -1:
                print('File content')
                print(file_content.index(serch))
                print('Line content: ', line)


print_file(file_name)

print_file2(file_name, 'test')
