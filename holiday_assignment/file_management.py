import os
import time

# 1. Create nested directories
path = "My_Project/assignments/task1"
os.makedirs(path, exist_ok=True)

# 2. Display current working directory
print("Current Working Directory:", os.getcwd())
print("Byte String Format:", os.getcwdb())

# 3. Create and write a file
file_path = os.path.join(path, "sample.py")

with open(file_path, "w") as file:
    file.write("print('Python Assignment')")

# 4. Check whether directory exists
print(os.path.isdir(path))

# 5. Calculate total file size
total_size = 0

for root, dirs, files in os.walk("My_Project"):
    for name in files:
        file_name = os.path.join(root, name)
        total_size += os.path.getsize(file_name)

print("Total Size:", total_size, "bytes")

# 6. Retrieve file timestamps
access_time = os.path.getatime(file_path)
modified_time = os.path.getmtime(file_path)

print("Access Time:", time.ctime(access_time))
print("Last Modified Time:", time.ctime(modified_time))

# 7. List directory contents
print("List of files:", os.listdir(path))