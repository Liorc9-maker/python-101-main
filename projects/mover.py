# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib
# Find the path to my Desktop
desktop = pathlib.Path('/Users/liorc/Desktop')
# Create a new folder
new_path = pathlib.Path('/Users/liorc/Desktop/Screenshots')
new_path.mkdir(exist_ok=True)
# Filter for screenshots only
for file in desktop.iterdir():
    if file.suffix.lower() ==  ".png":
        print(file)
        # Create a new path for each file
        new_filepath = new_path.joinpath(file.name)
        # Move the screenshot there
        file.replace(new_filepath)
# Move the screenshot there
