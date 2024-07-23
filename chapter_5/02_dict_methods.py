
###a.items(): Returns a list of (key,value)tuples.###

marks = {
    "sam":100,
    "swasti":200,
    "jon":300,
    20:"pal"
}
print(marks.items())


#### a.keys() and a.values(): Returns a list containing dictionary's keys and values respectivley ####

print(marks.keys())

print(marks.values())


##### a.update({"friends":}): Updates the dictionary with supplied key-value pairs.

marks.update({"sam":250,"leo":69})
print(marks)



###### a.get("name"): Returns the value of the specified keys


print(marks.get("sam"))
print(marks.get("jain"))        ## --> OUTPUT IS NONE
# print(marks["jain"])        ## --> SHOWING ERROR



### CLEAR ###      --->>> GIVES EMPTY DICT.
# marks.clear()
# print(marks)


### COPY #### ---> copy dict.
marks1 = marks.copy()
print(marks1)


### POP ###     --->>>>  remove specific item
marks.pop("sam")
print(marks)



## POP ITEM  ####       --->>> remove last add item
marks.popitem()
print(marks)


## LEN ###
print(len(marks))