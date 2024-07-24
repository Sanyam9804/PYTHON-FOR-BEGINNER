maths = int(input("ENTER YOUR MARKS MATHS : "))
english = int(input("ENTER YOUR MARKS ENGLSIH : "))
physics = int(input("ENTER YOUR MARKS PHYSICS : "))



if ((maths + english +physics)*40/100 >= 40):
    print("pass")
else:
    print("fail")



###### 3rd          METHOD ###########      -----> internal sunject passing criteria also ######


marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)
