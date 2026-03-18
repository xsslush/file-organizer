import os
import shutil

# list files from a directory
dir_path = r"Documents"
os.chdir(dir_path)
files = os.listdir(dir_path)
for file in files:
    print(file)