import os
import shutil
import pathlib
import tempfile
import zipfile
import fileinput

# 1. Retrieve file properties
def get_file_properties(file_path):
    file_stat = os.stat(file_path)
    return {
        "size": file_stat.st_size,
        "last_modified": file_stat.st_mtime,
        "is_file": os.path.isfile(file_path)
    }

# 2. Create directories
def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory {dir_path} created")

# 3. Match patterns in filenames
def match_pattern(directory, pattern):
    return list(pathlib.Path(directory).glob(pattern))

# 4. Traverse directory trees
def traverse_directory(root_dir):
    for root, dirs, files in os.walk(root_dir):
        print(f"Current Directory: {root}")
        print(f"Subdirectories: {dirs}")
        print(f"Files: {files}")

# 5. Make temporary files and directories
def create_temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Temporary file content")
        print(f"Temporary file created: {temp_file.name}")
        return temp_file.name

def create_temp_directory():
    temp_dir = tempfile.mkdtemp()
    print(f"Temporary directory created: {temp_dir}")
    return temp_dir

# 6. Delete files and directories
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    else:
        print("File not found")

def delete_directory(dir_path):
    shutil.rmtree(dir_path, ignore_errors=True)
    print(f"Deleted directory: {dir_path}")

# 7. Copy, move, or rename files and directories
def copy_file(src, dest):
    shutil.copy2(src, dest)
    print(f"Copied {src} to {dest}")

def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Moved {src} to {dest}")

def rename_file(src, dest):
    os.rename(src, dest)
    print(f"Renamed {src} to {dest}")

# 8. Create and extract ZIP archives
def create_zip(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
    print(f"Created ZIP archive: {zip_name}")

def extract_zip(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Extracted {zip_name} to {extract_to}")

# 9. Open multiple files using fileinput module
def read_multiple_files(files):
    with fileinput.input(files) as f:
        for line in f:
            print(line, end='')

# 10. Read and write text files
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_text_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Written to file: {file_path}")

# 11. Read and write CSV files
def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def write_csv_file(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"CSV file written: {file_path}")

# Example usage (Uncomment to run)
# create_directory("test_dir")
# temp_file = create_temp_file()
# delete_file(temp_file)
# create_zip("example.zip", ["file1.txt", "file2.txt"])
# extract_zip("example.zip", "extracted")
# write_text_file("example.txt", "Hello, World!")
# print(read_text_file("example.txt"))
# write_csv_file("data.csv", [["Name", "Age"], ["Alice", 30], ["Bob", 25]])
# read_csv_file("data.csv")
