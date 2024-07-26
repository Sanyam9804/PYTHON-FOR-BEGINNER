'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.

'''



with open("poem.txt", "r") as f:
    contents = f.read()
    if "twinkle" in contents:
        print("twinkle is present")
    else:
        print("twinkle is not present")
    print(contents)


 ### second method ### 
 
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()