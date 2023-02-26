file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

file1.writelines(L)
file1.close()

with open("myfile.txt", 'a') as f:
    f.write('End of the line\n')

with open("myfile.txt", 'r') as f:
    for i, lines in enumerate(f):
        print(lines.strip())
