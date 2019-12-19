# move_files_having_specific_extensions.py

# This Program moves files having user entered extensions to a specific folder

# Search all the directories in the folder for the filetype and display the filenames

# Take the path of the folder to move the files to from the user

# Display a message that the files have succesfully been moved to the 'destination'

import os , shutil

def compute(path, fileExt):
    if os.path.exists(path):          # checks if the path entered by the user exists
        print()
        print("The path exists")

        for foldername, subfolder, filename in os.walk(path):       # walks the each subfolder in the specified folder
            for file in filename:
                if file.endswith(fileExt):
                    print(os.path.join(foldername , file))
        print()
        sure_prompt = input("These files will be moved, are you sure? (Y/N) : ").strip().upper() # asks the user if he is sure about deleting the files

        if sure_prompt == 'Y':
            print()
            move_path = input("Enter the path to  move the files into : ")

            if os.path.exists(move_path):
                print()
                print("Moving......")

                for foldername, subfolder, filename in os.walk(path):       # walks the each subfolder in the specified folder
                    for file in filename:
                        if file.endswith(fileExt):
                            shutil.move(os.path.join(foldername , file) , os.path.join(move_path , file)) # moves the file to the specified location without chaanging its filename
                
                print("The files have succesfully been moved")

            else:
                print("The destination path does not exist !!!")


        elif sure_prompt == 'N':
            print("Skipping......")
            print()
        else:
            print("Wrong Input !!!")
            print()

    else:
        print("The path does not exist !")

            
if __name__ == '__main__':
    print("Text-based file moving program")
    print()

    path = input("Enter the full path of the folder to search : ")    # Take the path of folder to search from the user
    fileExt = input("Enter the extension of the file to search : ") # Take the file extension to search for from the user

    compute(path , fileExt)
