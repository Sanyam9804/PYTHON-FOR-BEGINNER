# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


a = int(input("ENTER YOUR MARKS : "))

if (a >= 90):
    print("EXCELLENT")
elif(a>80 and a<90):
    print("A")
elif(a>70 and a<80):
    print("B")
elif(a>60 and a<70):
    print("C")
elif(a>50 and a<60):
    print("D")
elif(a<=50):
    print("F")
    

print("YOUR GRADE IS",a)

#########                GOOD CODE              #########

marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)