# Exercise 3: Read the file and render only the data of people who passed the test

# Open our input file in a proper way, 'f' is a variable that represents our opened file
f = open ('./Exercise Files/inputFile.txt', 'r')
# Add the for loop to read the file line by line
for line in f:
    # Add a split function that splits a string into a list where each word is a list item
    line_split = line.split()
    # If the third item of the list (exam result) is equal to P (pass)
    if line_split[2] == 'P':
        # Print this line
        print(line)
f.close()