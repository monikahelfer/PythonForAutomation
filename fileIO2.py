# Exercise 2: Read the file and render a counter for each line

# Open our input file in a proper way, 'f' is a variable that represents our opened file
f = open ('./Exercise Files/inputFile.txt', 'r')
# Add a counter to count the number of lines and set it to 0 for the start
count = 0
# Add the for loop to read the file line by line
for line in f:
    # Print each line and render the counter at the beginning
    # The 'str()' function converts data into a string, otherwise it can't be rendered
    print(str(count) + ' ' + line)
    # Increase the counter to move to the next line
    count = count + 1
f.close()