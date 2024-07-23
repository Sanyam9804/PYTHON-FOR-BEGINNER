s = {1,5,3,43,"sam",3,3,3}


### ADD ####
s.add(45)    
print(s)


## LEN ##
print(len(s))


## REMOVE ##
s.remove(45)
print(s)


## POP ##
s.pop()
print(s)


## clear ##
s.clear()
print(s)


## union ##         ---->>> take all same as well as unique values from both sets 
q = {1,5,10,15}
t = {1,3,5,7,10,15}
print(q.union(t))


## INTESECTION ##       ---->>> take only same values from the both sets
print(q.intersection(t))


### SUBRACTION ON SET ###
print(q-t)


### issubset ##
q = {1,5,10,15}
t = {1,3,5,7,10,15}
print(q.issubset(t))
print(t.issubset(q))


## issuperset ##
x = {1,2,3,4}
y = {1,2,3}
print(x.issuperset(y))
print(y.issuperset(x))


