'''
self refers to the instance of the class. It is automatically passed with a function call
from an object.
'''

class employee:
    langugae = "py"
    salary = 1200000

    def getinfo(self):
        print(f"the langugae is : {self.langugae} the salary is {self.salary}")
  
    def greet(self):
        print("good day sir")
        
    @staticmethod                   ### staticmethod doesnt req. self 
    def greet():                    ###  Sometimes we need a function that does not use the self-parameter. We can define a                                    
        print("good day sir")        ###    static method like this:

sam = employee()
sam.langugae = "JAVA"               ## sam.langugae is INSTANCE ATTRIBUTES
print(sam.salary,sam.langugae)

print()

sam.getinfo()           ## -->> working employee.getinfo(sam)

print()

sam.greet()

print()

sam.greet()