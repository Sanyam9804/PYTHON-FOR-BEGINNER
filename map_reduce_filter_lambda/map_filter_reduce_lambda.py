### MAP FUNCTION ####

# MAP: map applies a function to each item in an iterable (like a list) and returns a new iterable with the results.

# Define a function to compute the cube of a number
def cube(x):
    return x * x * x

# Example usage of the cube function
print(cube(10))  # Output: 100

# List of numbers
lst = [1, 2, 3, 4, 5]

# Using map function to apply cube function to each element of lst
lst1 = list(map(cube, lst))
print(lst1)  # Output: [1, 8, 27, 64, 125]



### LAMBDA FUNCTION: ####

# LAMBDA: lambda functions are small anonymous functions defined using the lambda keyword, useful for short functions where defining a named function would be overkill.

# Lambda function examples

# Lambda function to add 10 to a number
x = lambda a: a + 10
print(x(5))  # Output: 15

# Lambda function to multiply two numbers
x = lambda c, d: c * d
print(x(10, 2))  # Output: 20

# Lambda function to perform a more complex operation
x = lambda s, t, u: s + t * u
print(x(10, 2, 3))  # Output: 16

# Lambda function returning another lambda function
def multi(n):
    return lambda a: a * n

mymulti = multi(2)  # Create a function that multiplies its argument by 2
print(mymulti(4))   # Output: 8

# Lambda function in map
lst = [1, 2, 3, 4, 5]
lst1 = list(map(lambda x: x * x * x, lst))
print(lst1)  # Output: [1, 8, 27, 64, 125]



### FILTER: ####

# FILTER: filter constructs a new iterable from those elements of the iterable for which a function returns True.

# Filter example

lst = [1, 2, 3, 4, 5]

# Function to filter numbers greater than 3
def filter_fun(a):
    return a > 3

result = list(filter(filter_fun, lst))
print(result)  # Output: [4, 5]



#### REDUCE: ####

# REDUCE: reduce applies a rolling computation to sequential pairs of values in an iterable, ultimately reducing them to a single value.

# Reduce example
from functools import reduce

# Computing the product of elements in a list using reduce and lambda function
numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # Output: Product: 120


# COMBINED USE OF MAP, REDUCE, AND FILTER:

# These examples illustrate how to leverage map, filter, and reduce along with lambda functions to perform operations on lists efficiently and concisely in Python


            # EXAMPLE 1:
        
from functools import reduce

# Example combining map, filter, and reduce

marks = [1, 2, 3, 4, 5, 6, 7]

# Filter even numbers, square them, and then sum using reduce
evens = filter(lambda a: a % 2 == 0, marks)
squares = map(lambda x: x ** 2, evens)
sum_of_squares = reduce(lambda x, y: x + y, squares)

print(sum_of_squares)  # Output: 120 (sum of squares of even numbers in marks)


                # EXAMPLE 2:
                
from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Double each number using map, filter out odd numbers using filter, and sum using reduce
result = reduce(lambda x, y: x + y,
                filter(lambda x: x % 2 == 0,
                       map(lambda x: x * 2, numbers)))

print("Result:", result)  # Output: 60 (sum of doubled even numbers in numbers)
