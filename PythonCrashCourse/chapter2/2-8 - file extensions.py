# file extensions

# python has a removesuffix() nmethod that works exactly like removeprefix(). Assign the 
# value 'python_notes.txt' to a variable called filename. Then use the removesuffix()
# method to display the filename without the file extension, flike some file browsers do.

filename = 'python_notes.txt'

print(f"{filename.removesuffix('.txt')}")