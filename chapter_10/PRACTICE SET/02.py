'''
2. Write a class “Calculator” capable of finding square, cube and square root of a
number.
'''

class Calculator:
    
    @staticmethod
    def calculate():
        a = int(input("ENTER YOUR NUMBER: "))
        
        sqr = a ** 2
        cubee = a ** 3
        squrt = a**1/2
        
        print(f"Square of your number is: {sqr}")
        print(f"Cube of your number is: {cubee}")
        print(f"Square root of your number is: {squrt}")


Calculator.calculate()


### 2nd method ###

class Calculator:
    def __init__(self, n):
        self.n = n  # Initialize an instance variable 'n' with the value passed during object creation
    
    def square(self):
        print(f"The square is {self.n * self.n}")  # Calculate and print the square of 'n'
    
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")  # Calculate and print the cube of 'n'
    
    def squareroot(self):
        print(f"The squareroot is {self.n ** 0.5}")  # Calculate and print the square root of 'n'


a = Calculator(4)   ### ### a = Calculator(int(input("ENTER YOUR NUMBER")))


a.square()



a.cube()

a.squareroot()


        
        
