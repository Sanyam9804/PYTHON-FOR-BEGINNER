## WITH STATEMENT :
    
## The best way to open and close the file automatically is the with statement


f = open("file_3.txt")

print(f.read())

f.close()

## the same function is written using the with statement like this:

with open("file_3.txt") as f:
    print(f.read())
    
# you dont have to explicitly close the file