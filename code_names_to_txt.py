# export_filenames.py
# Reads all filenames in a folder and saves them into a txt file

import os

# Change this to your folder path
folder_path = r"./2026-07-27"

# Output txt file
output_file = "filenames.txt"

# Get all files only
file_list = [
    file for file in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, file))
]

# Save filenames to txt
with open(output_file, "w", encoding="utf-8") as f:
    for file_name in file_list:
        f.write(file_name + "\n")

print(f"Saved {len(file_list)} filenames to {output_file}")