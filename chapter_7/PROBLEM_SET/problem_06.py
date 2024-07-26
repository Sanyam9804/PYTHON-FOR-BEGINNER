# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter the number: "))  # Takes user input and converts it to an integer
factorial = 1  # Initializes the factorial variable to 1

# Loop to calculate the factorial
for i in range(1, n + 1):
    factorial = factorial * i

# Output the result
print(f"The factorial of {n} is {factorial}")
