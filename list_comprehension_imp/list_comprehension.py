####### LIST COMPREHENSION ####

number = [1,2,3,4,5]
sq_no = [i**2 for i in number]          #### -->>> expression for item in iterable if condtion
print(sq_no)



#### even number ###

lst = [1,2,3,4,56,7,8,9,9,75]
even_no = [i for i in lst if i%2==0]
print(even_no)




#### flatenning list ####

a = [[1,2,3],[5,6,7],[8,9,0]]
b = [i for sublist in a for i in sublist]
print(b)



####### type casting ###

string = ["1","2","3"]
lst = [int(i) for i in string]
print(lst)


##### ZIP --->... add list element-wise ######

list1 = ["m","na","is"]
list2 = ["y","me","sam"]

list = [i+j for i,j in zip(list1,list2)]
print(list)