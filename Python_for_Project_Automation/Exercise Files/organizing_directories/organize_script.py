
import os
from pathlib import Path

# Define the subdirectories and their corresponding file suffixes
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}       

# Function to determine the appropriate directory for a given file type
def getDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"

# Test the getDirectory() function
print(getDirectory('.pdf'))  # Should return "DOCUMENTS"
#print(getDirectory('.mp3'))  # Should return "AUDIOS"
#print(getDirectory('.avi'))  # Should return "VIDEOS"

# Test the getDirectory() function
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = getDirectory(fileType)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# Test the organizeDirectory() function
organizeDirectory()



























# import os
# from pathlib import Path

# SUBDIRECTORIES = {
#     "DOCUMENTS": ['.pdf','.rtf','.txt'],
#     "AUDIOS": ['.m4a','.m4b','.mp3'],
#     "VIDEOS": ['.mov','.avi','.mp4'],
#     "IMAGES": ['.jpg','.jpeg','.png']
# }

# def pickDirectory(value):
#     for category, suffixes in SUBDIRECTORIES.items():
#         if value in suffixes:
#             return category
#     return "MISC"

# # test out the pickDirectory() function
# # uncomment this line and write your code

# def organizeDirectory():
#     for item in os.scandir():
#         if item.is_dir():
#             continue
#         filePath = Path(item)
#         fileType = filePath.suffix.lower()
#         directory = pickDirectory(fileType)
#         directoryPath = Path(directory)
#         if directoryPath.is_dir() != True:
#             directoryPath.mkdir()
#         filePath.rename(directoryPath.joinpath(filePath))

# # test out the organizeDirectory() function
# # uncomment this line and write your code