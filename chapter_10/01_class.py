class employee:                                     ### class -->> employee
    name = "sam"                            ### name,salary,langugae is --->> class attributes
    langugae = "py"
    salary = 1200000

a = employee()
print(a.name,a.langugae,a.salary)


class employee:
    langugae = "py"
    salary = 1200000

sam = employee()
print(sam.salary,sam.langugae)

swasti = employee()
print(swasti.salary,swasti.langugae)

 
sam = employee()
sam.name = "sam"                                        #### here name is object/instance atribute and salary and langugae are class atributes as they belong to class
print(sam.salary,sam.langugae,sam.name)

swasti = employee()
swasti.name = "swasti"                                  ### this is an object/instance atribute
print(swasti.salary,swasti.langugae,swasti.name)




