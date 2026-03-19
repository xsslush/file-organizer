import os 
import shutil

# list all files in the specified directory
files = os.listdir('/home/lush/Downloads/Test')
for file in files:
    print(file)

# check file extensions
for file in files:
    extension = os.path.splitext(file)[-1].lower()
    if extension == '.txt':
        print(file, 'is txt')
    elif extension == '.png':
        print(file, 'is png')
    elif extension == '.pdf':
        print(file, 'is pdf')
    else:
        print(file, 'unknown file format')

# create new folders
txt_directory = '/home/lush/Downloads/Test/TXT'
img_directory = '/home/lush/Downloads/Test/Images'
pdf_directory = '/home/lush/Downloads/Test/PDFs'
if not os.path.exists(txt_directory):
    os.mkdir(txt_directory)
    print(f'{txt_directory} directory created')
if not os.path.exists(img_directory):
    os.mkdir(img_directory)
    print(f'{img_directory} directory created')
if not os.path.exists(pdf_directory):
    os.mkdir(pdf_directory)
    print(f'{pdf_directory} directory created')

# moving files
for file in files:
    move = extension
    if move :
        shutil.move(file, )