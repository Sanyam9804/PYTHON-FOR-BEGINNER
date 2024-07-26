n = int(input("Enter the number: "))  # Input the size of the box (number of rows/columns)

for i in range(1, n+1):  # Loop through each row from 1 to n
    if i == 1 or i == n:  # If it's the first or last row
        print("*" * n, end="")  # Print a row of n asterisks
    else:
        print("*", end="")  # Print the first asterisk of the row
        print(" " * (n - 2), end="")  # Print (n - 2) spaces for the inner part of the row
        print("*", end="")  # Print the last asterisk of the row
    
    print("")  # Move to the next line for the next row
