from pathlib import Path

path = Path('C:\kaggle projects\\feedback_evaluation') # setting our posixpath obj to a var which can be used several times in our code

Path.cwd() # show the Current Working Directory

Path('sample_data/README.md').exists() # check if a directory or a file exists

Path('test_dir').mkdir() # creating a new dir

# A much easier syntax to 
# if not os.path.exists('test_dir'):
  #  os.mkdir('test_dir')
Path('test_dir').mkdir(parents=True, exist_ok=True) 
# when exist_ok=True, the FileExistsError is automatically ignored
#If parents is true, any missing parents of this path are created as needed

Path(os.path.join('test_dir', 'level_1b', 'level_2b', 'level_3b')).mkdir(parents=True, exist_ok=True) # creating a directory when its parent directories are not existing

list(Path("T:\Codes\Python\Basics").iterdir()) # get all the files in a specified dir

list(Path('T:\Codes\Python\Basics').glob('*.py')) # has built in glob lib to search for files i.e get all files in specified path with a .py extension

f = Path('test_dir/test.txt')
f.write_text('This is a sentence.') # for simple writing
f.read_text() # easily read a file

f.resolve() # returns the absolute path of the file
f.name # file name
f.stem # file name without extension
f.suffix # file extension
f.stat() # return the statistics, create/update time
f.stat().st_size # show the size of the file in bites


