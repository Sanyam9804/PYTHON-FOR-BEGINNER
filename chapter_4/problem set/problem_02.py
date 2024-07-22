# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner

stud1 = int(input("ENTER YOUR MARKS"))
stud2 = int(input("ENTER YOUR MARKS"))
stud3 = int(input("ENTER YOUR MARKS"))
stud4 = int(input("ENTER YOUR MARKS"))
stud5 = int(input("ENTER YOUR MARKS"))
stud6 = int(input("ENTER YOUR MARKS"))

stud_marks = [stud1,stud2,stud3,stud4,stud5,stud6]
stud_marks.sort()
print(stud_marks)

'''
marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)
'''
