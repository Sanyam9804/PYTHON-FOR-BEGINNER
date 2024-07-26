'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n

sum(n) = sum(n-1) + n           ---->>>> important
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(7))

########## 2nd method #####

# def natural_no():
#     n = int(input("Enter the number: "))

#     i = 1
#     total_sum = 0
#     while i <= n:
#         total_sum = total_sum + i
#         i = i + 1
    
#     print(f"The sum of the first {n} natural numbers is: {total_sum}")

# natural_no()
