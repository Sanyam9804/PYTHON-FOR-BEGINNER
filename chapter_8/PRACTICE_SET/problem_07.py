def rem(l, word):
    n = []  # Initialize an empty list to store modified elements
    for item in l:  # Iterate through each item in the list l
        if not (item == word):  # Check if the current item is not equal to the word to remove
            n.append(item.strip(word))  # Append the stripped item (remove occurrences of 'word') to list n
    return n  # Return the modified list n

# Example list
l = ["Harry", "Rohan", "Shubham", "an"]

# Call the rem function with list l and word "an"
print(rem(l, "an"))
