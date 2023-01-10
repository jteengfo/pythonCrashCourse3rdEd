'''
Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
'''

# import module name

import message 

message.display_message()

# from module_name import function_name

from message import display_message

display_message()

# from module_name import function_name as fn

from message import display_message as dm

dm()

# import module_name as mn

import message as mn

mn.display_message()

# from module_name import *

from message import *

display_message()