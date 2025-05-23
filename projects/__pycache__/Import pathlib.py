# Import pathlib
import pathlib
# Find the path to my Desktop
desktop = pathlib.Path('/Users/liorc/Desktop')
# Create a new folder
new_path = pathlib.Path('/Users/liorc/Desktop/screenshots')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
# Filter for screenshots only
    if filepath.suffix == '.png':
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshots in there
        filepath.replace(new_filepath)