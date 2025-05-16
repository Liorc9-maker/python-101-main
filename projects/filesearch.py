# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
import pathlib

base_path = pathlib.Path('/Users/liorc/Desktop/recycling amma')

jpg_files = []
all_extensions = set()

for item in base_path.iterdir():
    if item.is_file():
        if item.suffix.lower() == ".jpg":
            jpg_files.append(item.resolve())
            all_extensions.add(item.suffix.lower())

    elif item.is_dir():
        for subitem in item.iterdir():
            if subitem.is_file():
                if subitem.suffix.lower() == ".jpg":
                    jpg_files.append(subitem.resolve())
                    all_extensions.add(subitem.suffix.lower())

    elif subitem.is_dir():
        for subsubitem in subitem.iterdir():
            if subsubitem.suffix.lower() == ".jpg":
                jpg_files.append(subsubitem.resolve())
                all_extensions.add(subsubitem.suffix.lower())

print("List of JPG files:")
for jpg in jpg_files:
    print(jpg)

print("\nAll file extensions found:")
print(all_extensions)          