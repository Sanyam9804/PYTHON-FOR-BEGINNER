    ## 5. Repeat program 4 for a list of such words to be censored. ##
    
words = ["Donkey", "bad", "ganda"]

with open("file_donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)
    
    
# List of words to censor
words = ["Donkey", "bad", "ganda"]

# Open file for reading
with open("file_donkey.txt", "r") as f:
    # Read entire content of the file into 'content'
    content = f.read()

# Iterate over each word in 'words' list
for word in words:
    # Replace each occurrence of 'word' with '#' repeated 'len(word)' times
    content = content.replace(word, "#" * len(word))

# Open file for writing
with open("file.txt", "w") as f:
    # Write modified content back to 'file.txt'
    f.write(content)
