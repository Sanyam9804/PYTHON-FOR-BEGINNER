n = int(input("Enter the number: "))  # Input the number of lines to print

for i in range(1, n+1):  # Loop through each line from 1 to n
    print("*" * i, end="")  # Print i number of asterisks in the current line
    print("")  # Move to the next line for the next iteration