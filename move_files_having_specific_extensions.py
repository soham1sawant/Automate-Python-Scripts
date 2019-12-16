# move_files_having_specific_extensions.py

# This Program moves files having user entered extensions to a specific folder

# TODO : Search all the directories in the folder for the filetype and display the filenames

# TODO : Take the path of the folder to move the files to from the user

# TODO : Display a message that the files have succesfully been moved to the 'destination'

import os

def compute(path, fileExt):
    if os.path.exists(path):          # checks if the path entered by the user exists
        print("The path exists")

        for foldername, subfolder, filename in os.walk(path):
            print("The folder is : " + foldername)
            print("The subfolders in " + foldername + " are : " + str(subfolder) )
            print("The files in " + subfolder + " are : " + str(filename) )
    else:
        print('The path does not exist')

if __name__ == '__main__':
    print("Text-based file moving program")
    print()

    path = input("Enter the full path of the folder to search : ")    # Take the path of folder to search from the user
    fileExt = input("Enter the extension of the file to serach : ") # Take the file extension to search for from the user

    compute(path , fileExt)
