n = int(input("Enter a number: "))  # Input a number from the user

for i in range(2, n):  # Iterate through numbers from 2 to n-1
    if n % i == 0:  # Check if n is divisible by i (i.e., i is a factor of n)
        print("Number is not prime")  # If n is divisible by any number in this range, it's not prime
        break  # Exit the loop early because we've found a divisor

else:
    print("Number is prime")  # If no divisors were found in the range, n is prime



