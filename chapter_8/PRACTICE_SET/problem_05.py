def pattern(n):
    # Base case: if n is 0, exit the function
    if n == 0:
        return
    
    # Print a line of n stars ('*')
    print("*" * n)
    
    # Recursive call with n-1 to continue printing pattern
    pattern(n - 1)

# Call the pattern function with n = 3 to start the pattern printing
pattern(3)
