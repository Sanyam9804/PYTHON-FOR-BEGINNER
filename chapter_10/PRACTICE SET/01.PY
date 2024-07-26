'''
1. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
'''

class Programmer:
    
    def __init__(self,name,salary,language):                     ### dunder method  which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        self.company = "Microsoft"

a = Programmer("SAM",120,"JAVA")
print(a.name,a.salary,a.language,a.company)

b = Programmer("SWASTI",150,"PYTHON")
print(b.name,b.salary,b.language,b.company)

c = Programmer("SHUBHAM",180,"RUBY")
print(c.name,c.salary,c.language,c.company)


print()

##### other method #####

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 245001)
print(r.name, r.salary, r.pin, r.company)