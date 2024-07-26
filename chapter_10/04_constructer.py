class employee:
    langugae = "py"
    salary = 1200000
    
    def __init__(self,name,salary,language):                     ### dunder method  which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        
        print("I am creating an object")
        

    def getinfo(self):
        print(f"the langugae is : {self.langugae} the salary is {self.salary}")
  
    def greet(self):
        print("good day sir")
        
    @staticmethod
    def greet():
        print("good day sir")
        
a = employee
a.name = "Sam"
print(a.langugae,a.salary,a.name)

a.greet()

print()

a = employee("swasti",12999,"js")
print(a.name,a.salary,a.langugae)