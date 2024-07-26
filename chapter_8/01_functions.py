'''
A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of

'''
# FUNCTION DEFINATION

def avg():
    a = int(input("ENTER YOUR NUMBER: "))
    b = int(input("ENTER YOUR NUMBER: "))
    c = int(input("ENTER YOUR NUMBER: "))
    
    average = (a+b+c)/3
    print(average)
    
avg()   #--> FUNCTION CALL               #for multiple use same use avg()multiple time
print("THANK YOU")
#avg()
#avg()
#avg()
#avg()
#avg()



### 2nd method -->>> for average


def avg(input_list):
    avg = sum(input_list) / len(input_list)
    return avg
    
list = avg([1,2,3,4])
print(list)

'''

There are two types of functions in python:
• Built in functions (Already present in python)
• User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc.
The func1() function we defined is an example of user defined function

'''