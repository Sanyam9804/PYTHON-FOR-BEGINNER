a = [1,"sam","jain",2004]

i = 0
while(i<len(a)):
    print(a[i])
    i = i+1
    
    
    
##### LSIT ODD EVEN CHECK ####


list_ = [3,4,8,10,50]

index  = 0
while(index<len(list_)):
    element = list_[index]
    if element %2 == 0:
        print("EVEN NUMBER")
    else :
        print("ODD NUMBER")
    index += 1