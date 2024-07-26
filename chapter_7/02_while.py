####### WHILE LOOP #######
i = 1
while(i<6):
    print(i)
    i += 1          ### --> i = i+1 --->same 
    
    '''
    OUTPUT :
    1
    2
    3
    4
    5
    '''
 
a = 0
while(a<5):
    print("SAM")
    a += 1
    
    
i = 1
while i < 50:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
    i = i + 1



#### SQUARING THE L ITEMS AND ADD IN L2

l = [1, 2, 3]
l1 = []
i = 0

while i < len(l):
    l1 += [l[i] ** 2]
    i += 1

print("Original list:", l)
print("List of squares:", l1)

#### SQUARING THE L ITEMS AND ADD IN L2 -->>.  METHOD 2nd

l = [1, 2, 3]
l1 = []
i = 0

while i < len(l):
    l1.append(l[i] ** 2)
    i += 1

print("Original list:", l)
print("List of squares:", l1)


#### list indexing 

l1 = ["zebra", "cow", "dog", "cat", "pet"]
a = 0

while a < len(l1):  # Use < instead of in to compare a with the length of l1
    print(l1[a])
    print(a)  # Print the index a instead of i
    a = a + 1


### list character coutning 
l1 = ["zebra", "cow", "dog", "cat", "pet"]
a = 0

while a < len(l1):
    print(f"{l1[a]} is of {len(l1[a])} characters")
    a = a + 1

### list character coutning  --> 2nd method

l1 = ["zebra", "cow", "dog", "cat", "pet"]
index = 0

while index < len(l1):
    element = l1[index]  # Access the element at the current index
    print(len(element))  # Print the length of the current element
    index = index + 1  # Move to the next index

