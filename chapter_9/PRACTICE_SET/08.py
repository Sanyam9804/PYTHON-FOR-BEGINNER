# 8. Write a program to make a copy of a text file “this.txt”

with open("this.txt") as f:
    content = f.read()
    print(content)
    
with open("this_1.txt","w") as f:
    f.write(content)