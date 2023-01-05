'''
: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.

'''

pet = 'dog'
color = 'green'
name = 'james'
id = 123456789
password = '!_hehe good'

# True
print("Is pet == 'dog'? I predict True")
print(pet == 'dog')

print("\nIs color == 'green'? I predict True")
print(color == 'green')

print("\nIs name == 'james'? I predict True")
print(name == 'james')

print("\nIs id == 123456789? I predict True")
print(id == 123456789)

print("\nIs password = '!_hehe good'? I predict True")
print(password == '!_hehe good')

# False
print("\nIs pet == 'cat'? I predict False")
print(pet == 'cat')

print("\nIs pet == 'Dog'? I predict False")
print(pet == 'Dog')

print("\nIs name == 'James'? I predict False")
print(name == 'James')

print("\nIs password == '!_hehegood'? I predict False")
print(password == '!_hehegood')

print("\nIs id == 12346789? I predict False")
print(id == 12345789)