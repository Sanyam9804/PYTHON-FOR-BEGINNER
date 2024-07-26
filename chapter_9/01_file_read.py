'''
a = " very long email list "

emails = []
3 second mein code run hua
'''

'''
TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.
'''

f = open("file_1.txt","r")        ## r stands for read mode

data = f.read()  # Corrected method to read file contents

print(data)

f.close()  # Corrected method to close the file     imp f.close is a good practice

