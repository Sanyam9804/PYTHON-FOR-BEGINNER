def inches_to_cm():
    n = int(input("ENTER INCHES VALUE"))
    b = n*2.54
    print(b)
    
inches_to_cm()




#### 2nd method ---->>>  inche to cm <<<------

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")