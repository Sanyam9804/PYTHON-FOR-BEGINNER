'''
4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 
'''


with open("file_donkey.txt", "r") as f:
    content = f.read()
    if "donkey" in content:
        content = content.replace("donkey", "#####")
        print(content)
    else:
        print("no error")

with open("file_donkey.txt", "w") as f:
    f.write(content)



### 2nd method

word = "Donkey"

with open("file_donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(contentNew)
