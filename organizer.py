import os 
import shutil

# list all files in the specified directory
files = os.listdir('/home/lush/Downloads/Test')
for file in files:
    print(file)

txt_directory = '/home/lush/Downloads/Test/TXT'
media_directory = '/home/lush/Downloads/Test/Media'
pdf_directory = '/home/lush/Downloads/Test/PDFs'

# create new folders
if not os.path.exists(txt_directory):
    os.mkdir(txt_directory)
    print(f'{txt_directory} directory created')
if not os.path.exists(media_directory):
    os.mkdir(media_directory)
    print(f'{media_directory} directory created')
if not os.path.exists(pdf_directory):
    os.mkdir(pdf_directory)
    print(f'{pdf_directory} directory created')

# check file extensions + moving files
files_test = '/home/lush/Downloads/Test'
for file in files:
    extension = os.path.splitext(file)[-1].lower()
    if extension.endswith('.txt'):
        source_path = os.path.join(files_test, file)
        destination = os.path.join(txt_directory, file)
        if os.path.exists(destination):
            print('file already exists')
        shutil.move(source_path, txt_directory)
        print(file, 'moved to its directory')
    elif extension.endswith('.png'):
        source_path = os.path.join(files_test, file)
        destination = os.path.join(media_directory, file)
        if os.path.exists(destination):
            print('file already exists')
        shutil.move(source_path, media_directory)
        print(file, 'moved to its directory')
    elif extension.endswith('.pdf'):
        source_path = os.path.join(files_test, file)
        destination = os.path.join(pdf_directory, file)
        if os.path.exists(destination):
            print('file already exists')
        shutil.move(source_path, pdf_directory)
        print(file, 'moved to its directory')
    else:
        print(file, 'unknown file format')