# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
from pathlib import Path
# Run it in your labs folder and add formatting for nicer viewing.
root_folder = Path() 
if not root_folder.exists():
    print(f"Folder not found: {root_folder.name}")
else:
    print(f"Searching Python files in: {root_folder}\n")
    for py_file in root_folder.rglob("*.py"):
        print(f" {py_file.relative_to(root_folder)}")
