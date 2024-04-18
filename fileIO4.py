# Exercise 4: Manage the content of the file and save it in a new file

# Open our input file to read its content
f = open ('./Exercise Files/inputFile.txt', 'r')
# Create a new file that will allow pushing content into it ('w' means 'write')
passFile = open('./Exercise Files/PassFile.txt', 'w')
# Add the for loop to read the file line by line
for line in f:
    # Add a split function that splits a string into a list where each word is a list item
    line_split = line.split()
    # If the third item of the list (exam result) is equal to P (pass)
    if line_split[2] == 'P':
        # Add this line to the file
        # We use the 'write' function on the file. The function takes one argument: the data that should be added to the file
        passFile.write(line)
# Close both files
f.close()
passFile.close()