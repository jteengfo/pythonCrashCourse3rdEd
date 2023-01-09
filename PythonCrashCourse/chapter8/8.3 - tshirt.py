'''
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''

def make_shirt(size, message):
    print(f"Selected {size} for size...")
    print(f"Printing the message: '{message.title()}' to the shirt.")

# using positional arguments
make_shirt('medium', 'hello world')

# using keyword arguments
make_shirt(size='large', message='hello world')