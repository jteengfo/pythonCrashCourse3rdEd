'''
You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

# test for equality and inequality with string 

string = 'abcde'
print("is string == 'abcde? I predict True")
print(string == 'abcde')

print("is string == 'abcdE'? I predict False")
print(string == 'abcdE')


# test using lower method
string = 'ABCDE'
string = string.lower()
print("is string == 'abcde'? I predict True")
print(string == 'abcde')

print("is string == 'ABCDE'? I predict False")
print(string == 'ABCDE')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
num = 10

print("is num = 10? I predict True")
print(num == 10)

print("is num != 10? I predict False")
print(num != 10)

print("is num > 10? I predict False")
print(num > 10)

print("is num < 10? I predict False")
print(num < 10)

print("is num >= 10? I predict True")
print(num >= 10)

print("is num <= 10> I predict True")
print(num <= 10)


# Tests using the and keyword and the or keyword
letter = 'a'

print("is letter 'a' and 'A'? I predict False")
print(letter == 'a' and letter == 'A')

print("is letter 'a' or 'A'? I predict True")
print(letter == 'a' or letter == 'A')

# Test whether an item is in a list

list = [1,2,3,4,5]
num = 4
print("is 4 in the list? I predict True")
if num in list:
    print("True")
else: 
    print("False")

# Test whether an item is not in a list
print("is 9 in the list ? I predict False")
num2 = 9

if num2 in list:
    print("True")
else: 
    print("False")
