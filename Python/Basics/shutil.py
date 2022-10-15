import shutil

#* shutil copy 
#* Preserves file permissions
#* Destination can be a directory
#* Does not copy metadata
#* Does not work with File objects

shutil.copy('shutil.txt', 'shutil2.txt') # Copy file into a new file; creates a new file if path does not exist
shutil.copy('shutil.txt', 'models/') # Copy file into a new folder; path must exist
shutil.copy('shutil.txt', 'C:\kaggle projects\\feedback_evaluation')

#* shutil copyfile
#* Does not preserve file permissions
#* Destination cannot be a directory
#* Does not copy metadata
#* Does not work with File objects

shutil.copyfile('shutil.txt', 'shutil4.txt')
shutil.copyfile('shutil.txt', 'shutil3.txt', follow_symlinks=True)

#* shutil copy2
#* identical to shutil.copy() except that copy2() attempts to preserve file metadata as well

shutil.copy2('shutil.txt', 'shutil5.txt') 

#* shutil copyfileobj
#* Does not preserve file permissions
#* Destination cannot be a directory
#* Does not copy metadata
#* Can work with File objects

source_file = open('shutil.txt', 'rb')
dest_file = open('shutil-binary.txt', 'wb')

shutil.copyfileobj(source_file, dest_file)

shutil.move('file directory', 'destination directory') # move a file or folder to a new path
