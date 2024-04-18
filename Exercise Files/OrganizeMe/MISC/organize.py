# A dictionary containing four categories and a list for each category that contains the possible file types
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# A function that checks the file suffix and based on the suffix returns its category
def pickDirectory(value):
    # Here we have the for loop that takes two variables as parameters (it's possible for dictionaries and lists)
    # In the case of dictionaries, the first parameter is a key and the second is a value 
    # We can add any names of parameters, they don't matter, but the dictionary name after 'in' is important and needs to be defined earlier
    # The items function gives us access to keys of the dictionary (our categories)
    for category, suffixes in SUBDIRECTORIES.items():
        # We iterate through our second parameter (value of each key) to access suffixes in each list
        for suffix in suffixes:
            # If you find in any category a suffix that matches the provided parameter, tell me which category it is
            if suffix == value:
                return category

# Print the result of our function to check the category of pdf
print(pickDirectory('.pdf'))
print(pickDirectory('.avi'))