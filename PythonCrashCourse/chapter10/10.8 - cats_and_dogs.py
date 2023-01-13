'''
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
executes properly.'''

from pathlib import Path

cat_path = Path('cats.txt')
dog_path = Path('dogs.txt')

cat_names = 'kitty\ntom\nkilo\n'
dog_names = 'bull\nmilo\nodin'

cat_path.write_text(cat_names)
dog_path.write_text(dog_names)


try: 
    cat_names = cat_path.read_text()
    dog_names = dog_path.read_text()
except FileNotFoundError:
    print("Sorry one of the files cannot be found.")
else:
    print(cat_names.title())
    print(dog_names.title())