# create_files_from_txt.py
# Creates files from names listed in a txt file

input_file = "filenames.txt"

with open(input_file, "r", encoding="utf-8") as f:
    file_names = [line.strip() for line in f if line.strip()]

for file_name in file_names:
    with open(file_name, "w", encoding="utf-8") as file:
        pass  # creates empty file

print(f"Created {len(file_names)} files")
