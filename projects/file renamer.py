import pathlib

# Set the target folder path
path = pathlib.Path('/Users/liorc/Desktop/recycling amma')

# Define a base name for the renamed files
base_name = "image"

# Start a counter
counter = 1

# Use rglob('*') to recursively go through all files
for file in path.rglob('*'):
    if file.is_file():
        # Get the file extension (e.g., .jpg, .png)
        extension = file.suffix.lower()

        # Build new file name (keep in the same directory)
        new_name = f"{base_name}_{counter:03}{extension}"
        new_path = file.parent / new_name

        # Rename the file
        file.rename(new_path)

        print(f"Renamed: {file} -> {new_path}")
        counter += 1
