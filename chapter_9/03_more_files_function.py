f = open("file_3.txt","r")

### readlines function ####



# lines = f.readlines()

# print(lines,type(lines))

# f.close()



### readline function ####


# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))                  
                                    ### stops automatically when a empty string found means line 4 is not present but an empty string will present
# f.close()


### read line using while loop ##

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
     
f.close()