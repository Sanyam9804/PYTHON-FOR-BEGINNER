a = int(input("enter your number"))

i = 1
for i in range(1,11):
    table = a*i
    print(f"{a}*{i}={table}")
    i = i+1
    
    
## other method ####

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")