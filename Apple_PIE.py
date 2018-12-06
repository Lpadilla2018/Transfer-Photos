# Apple_Pie.py
#  01/25/2018
#  Developed by Louie Padilla

"""
Extract JPG files from folder, create a new folder according to object ID number and place extracted photos in
proper folders.

"""

import os
from shutil import move
from datetime import datetime


def main():
    # Ask user for path of photos that need to be moved. EX: C:\Users\Download\PhotoLocation
    def getFilePath():
        file_path = raw_input("Path of Target Photos: ")
        return file_path

    FILE_PATH = getFilePath()
    f = os.listdir(FILE_PATH)

    print('Apple PIE is ready!''\nProgram Executed on {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))

    # Check if folder has been made. If not, create new folder with name. Else, files will be placed in existing folder.
    def create_folder(name):
        new_path = r'{}\{}'.format(FILE_PATH, name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        return new_path

    # Iterate through folder where photos to be moved is located. Go through and look for a jpeg file. Checks if a
    # folder with the 'Object ID' name is created then moves files in proper folder.
    for jpg_file in f:
        folder_name = jpg_file.split("_")[1]
        new__folder = create_folder(folder_name)
        print new__folder
        if jpg_file.endswith(".jpg") or jpg_file.endswith(".jpeg"):
            source_path = (os.path.join(FILE_PATH, jpg_file))
            print source_path
            move(source_path, new__folder)

    print('Process completed on {}!'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))


if __name__ == '__main__':
    main()
