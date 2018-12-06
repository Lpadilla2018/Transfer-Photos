# Cherry Pie.py
# 11/30/2018
# Developed by Louie Padilla


"""
Loop through main folder directory. For each file in a folder rename file to folderName_snapshot_#.jpg

"""

# Import modules
import os
from shutil import move


######################################################################################################

INPUT_DESTINATION = raw_input(
    'Enter DESTINATION folder path\nEx. "C:\Users\Download\Destination": ')

INPUT_SOURCE = raw_input(
    'Enter SOURCE folder path\nEx. "C:\Users\Download\Source": ')


DESTINATION_FILE_PATH = r"{}".format(INPUT_DESTINATION)
SOURCE_FOLDER_PATH = r"{}".format(INPUT_SOURCE)


def create_folder(destination, name):
    new_path = r'{}\{}'.format(destination, name)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    return new_path


def copy_files(folderName):

    folderPath = r"{}\\{}".format(SOURCE_FOLDER_PATH, folderName)
    count = 1
    f = os.listdir(folderPath)
    new_folder = create_folder(DESTINATION_FILE_PATH, folderName)
    for name in f:
        if name.endswith(".jpg"):
            source_path = (os.path.join(folderPath, name))
            newName = "{}_snapshot_{}.jpg".format(name.split("_")[0], count)
            move(source_path, new_folder + "\\" + newName)
        count = count + 1


# Main Function
def transfer_files():
    # print(DESTINATION_FILE_PATH)
    # gets folder paths
    for root, dirs, files in os.walk(SOURCE_FOLDER_PATH):
        for folder in dirs:
            copy_files(str(folder))
            print(folder)


transfer_files()


#############################################################################################################
