a = int(input("Enter your number a: "))
b = int(input("Enter your number b: "))
c = int(input("Enter your number c: "))
d = int(input("Enter your number d: "))

if a > b and a > c and a > d:
    print("A is greater")
elif b > a and b > c and b > d:
    print("B is greater")
elif c > a and c > b and c > d:
    print("C is greater")
else:
    print("D is greater")
