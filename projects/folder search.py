import pathlib

# Specify the path to search
path = pathlib.Path('/Users/liorc/Desktop/recycling amma')
print(f"Searching in: {path}")

# List to store .jpg file paths
jpg_files = []

# Optional: Set to collect all file extensions
file_extensions = set()

# Loop through current folder (level 0), and subfolders (levels 1 and 2)
for item in path.iterdir():
    if item.is_file():
        if item.suffix.lower() == '.jpg':
            jpg_files.append(item.resolve())
        file_extensions.add(item.suffix.lower())
    
    elif item.is_dir():
        # Level 1
        for subitem in item.iterdir():
            if subitem.is_file():
                if subitem.suffix.lower() == '.jpg':
                    jpg_files.append(subitem.resolve())
                file_extensions.add(subitem.suffix.lower())
            
            elif subitem.is_dir():
                # Level 2
                for subsubitem in subitem.iterdir():
                    if subsubitem.is_file():
                        if subsubitem.suffix.lower() == '.jpg':
                            jpg_files.append(subsubitem.resolve())
                        file_extensions.add(subsubitem.suffix.lower())

# Print results
print("\nList of .jpg files found:")
for file in jpg_files:
    print(file)

print("\nUnique file extensions found:")
print(file_extensions)