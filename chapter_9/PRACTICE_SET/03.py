'''
3. Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.

'''
    
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


 

for i in range(2, 21):
    generateTable(i)
    
    
    
def generateTable(n):
    # Initialize an empty string to store the table
    table = ""
    
    # Loop from 1 to 10 (inclusive)
    for i in range(1, 11):
        # Generate each line in the table in the format "n X i = n*i"
        table += f"{n} X {i} = {n*i}\n"
    
    # Open a file in write mode (creates a new file or overwrites existing)
    with open(f"tables/table_{n}.txt", "w") as f:
        # Write the generated table string to the file
        f.write(table)

# Loop through numbers from 2 to 20 (inclusive)
for i in range(2, 21):
    # Call generateTable function for each number in the range
    generateTable(i)
