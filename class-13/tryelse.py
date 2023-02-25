import os


try:
    fn = open("text.txt", 'r')
    fn.write("This is my test file for exception handling!!!")
except IOError:
    print("Error: can find file or read data")
else:
    print("Written content in the file successfully")