'''
9. Write a program to find out whether a file is identical & matches the content of
another file.
'''

with open("sample1.txt") as f:
    content1 = f.read()
    print(content1)
    
with open("sample2.txt") as f:
    content2 = f.read()
    print(content2)
    
if (content1 == content2):
    print("BOTH FILE ARE IDENTICAL TO EACH OTHER")
else:
    print("BOTH FILE ARE NOT IDENTICAL TO EACH OTHER")
