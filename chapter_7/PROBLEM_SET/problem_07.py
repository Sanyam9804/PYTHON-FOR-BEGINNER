n = int(input("Enter the number: "))  # Input the number of rows for the pyramid

for i in range(1, n+1):  # Loop through each row from 1 to n
    print(" " * (n - i), end="")  # Print leading spaces to center the pyramid
    print("*" * (2 * i - 1), end="")  # Print asterisks for the current row
    print("")  # Move to the next line for the next row

    


