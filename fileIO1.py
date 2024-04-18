# Exercise 1: Read the file and render its whole content

# Open our input file in a proper way
# The open function doesn't require any imports and takes two parameters: an input file and the type of interaction ('r' means 'read')
f = open ('./Exercise Files/inputFile.txt', 'r')
# Check if it can read the file
# Print prints the file content in the terminal, f is the file, and we added the read function to read the file.
print(f.read())
# Close the file 
f.close()
# To run the code, type in the terminal 'python3 fileIO1.py' - it runs the file that contains our code