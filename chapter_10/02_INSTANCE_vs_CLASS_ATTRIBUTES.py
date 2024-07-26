class employee:                                    
    name = "sam"                         
    langugae = "py"
    salary = 1200000

a = employee()
print(a.name,a.langugae,a.salary)


class employee:
    langugae = "py"
    salary = 1200000

sam = employee()
sam.langugae = "JAVA"               ## sam.langugae is INSTANCE ATTRIBUTES
print(sam.salary,sam.langugae)

'''
Note: Instance attributes, take preference over class attributes during assignment &
retrieval.
'''

swasti = employee()
print(swasti.salary,swasti.langugae)