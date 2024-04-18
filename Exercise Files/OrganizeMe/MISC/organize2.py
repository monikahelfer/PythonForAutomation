import os
# We import a specific element of the pathlib module, so we can use it as 'Path', not 'pathlib.Path'
from pathlib import Path

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
    return 'MISC'

def organizeDirectory():
    # The OS module provides functions for interacting with the operating system
    # The scandir method scans the directory and returns directory entries
    # The for loop here scans the directory in which we have this file and checks each item
    # Each item seems to be a file path
    for item in os.scandir():
        # Checks whether the item is a directory
        if item.is_dir():
            # If it is a directory, start a new iteration of the loop to move to the next item
            # as we're not interested in organizing directories but files
            continue
        # We use the pathlib module to use the Path object that returns the item path and assigns the file path to a variable
        # Create a new variable for storing the path of the current item
        filePath = Path(item)
        # Now we define file type based on its suffix
        # The path contains the file name and extension at the end, so we can use to to get the suffix
        # The suffix attribute of the pathlib module accesses the file extension
        # Lower converts the extension to lowercase (don't know why)
        fileType = filePath.suffix.lower()
        # We use the pickDirectory function here for each file and provide its suffix/fileType as a parameter
        # This function returns the proper category, so directory equals to the category the file belongs to
        directory = pickDirectory(fileType)
        # We add the category as a file path that will be a part of the new path
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            # If such directory (for a specific category) doesn't exist, create it
            directoryPath.mkdir()
        # Rename the file file path to change it and therefore move the file. The rename function of pathlib changes the file name.
        # The file paths seem to be relative, which means that the file path is really a file name, so adding it to the directory path
        # changes the path to actual path of the file in the directory
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()