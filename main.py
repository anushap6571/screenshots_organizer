import os
import shutil
from pathlib import Path
#from PIL import Image

# store the screenshot directory path name
# can be any foldername you want 
ss_directory_path = "/Users/anushapatel/Desktop/Screenshots"
desktop_directory_path = "/Users/anushapatel/Desktop"


# check if the directory exists
# if it does not already exists, create a new folder with the name
if os.path.exists(ss_directory_path) == False:
    print("The directory does not exists.")
    os.mkdir(ss_directory_path)

# change to desktop directory
os.chdir(desktop_directory_path)

# function returns true if file is a screenshot
def is_screenshot(file):
    name, ext = os.path.splitext(file)
    list_of_words = name.split(" ")
    return (ext in ".png") and "Screenshot" == list_of_words[0]
    
# loop through each screenshot in the file, open it, and prompt for a new name, then close it and 
# move it to the Screenshots folder
for file in os.listdir():
    if(is_screenshot(file)):
        print(file)
        #image = Image.open(file)
        #image.show()
        new_name = input("Rename the Screenshot: ")
        new_name += ".png"
        os.rename(file, new_name)
        shutil.move(new_name, ss_directory_path)
        #image.close()
    