'''
Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches
'''

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)



