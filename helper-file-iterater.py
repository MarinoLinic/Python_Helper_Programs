import os
import pathlib
import random
from natsort import natsorted # sorts elements properly, ie. numerically

ADDRESS = "C:/Users/user/Desktop/NavalWars/NavalWars/frontend/public/avatars"
NUM_FILES = len(os.listdir(ADDRESS))

print("Directory: " + ADDRESS)
print("Number of files in directory: " + str(NUM_FILES))

num = 1

os.chdir(ADDRESS) # Change working directory
# random.randint(1, 1000000000)

for path in pathlib.Path(ADDRESS).iterdir():
    if path.is_file():
        # old_name = path.stem
        extension = path.suffix
        directory = path.parent

        # Windows won't allow you to have identical names of files, even for a moment, so we're
        # first renaming them to something we later won't get a match to
        error_safe_name = "test" + str(num) + extension
        path.rename(pathlib.Path(directory, error_safe_name))

        num += 1

num = 1
for path in pathlib.Path(ADDRESS).iterdir():
    if path.is_file():
        # old_name = path.stem
        extension = path.suffix
        directory = path.parent

        # print(path)

        new_name = str(num) + extension
        path.rename(pathlib.Path(directory, new_name))

        num += 1

print("Working directory: " + os.getcwd())

arr = natsorted(os.listdir())

print("export const characterImgAvatars = [")

for i in arr:
    print("\t\'/avatars/" + i + "\',")

print("]")

