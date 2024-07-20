#### len ####

name = "sanyam"
print(len(name))



### endswith ####

name = "sanyam"
print(name.endswith("yam"))
print(name.endswith("gam"))



### startswith ####

name = "sanyam"

print(name.startswith("san"))
print(name.startswith("yan"))



### CAPITALIZE #### -->>> capital first alphabet of first word only

print(name.capitalize())



## UPPER CASE ####  --->>>> capital whole words
print(name.upper())



## LOWER CASE ##        ---->>>> lower case whole words
print(name.lower())



## Title ##    --->>>> capital first alph. of each word

b = "my name is sanyam"
print(b.title())



## Index ## 

c = "my name is jon"
index = c.find("is")
print(index)



## REPLACE ###

d = "love udaipur"
print(d)
replace_string = d.replace("udaipur","kasol")
print(replace_string)



## find ## -->>> TO FIND ANYTHING OF THE STRING

name = "sam is a good  boy"
print(name.find("  "))

