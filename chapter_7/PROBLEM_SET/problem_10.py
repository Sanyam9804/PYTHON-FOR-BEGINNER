n = int(input("enter your number"))

for i in range(10,0,-1):
    print(f"{n}*{i}={n*i}")
    i = i-1
    
    
    
## 2nd method ##

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")