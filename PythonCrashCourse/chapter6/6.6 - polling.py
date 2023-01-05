'''
Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

'''

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

list = ['laura', 'jamie', 'emma', 'sarah', 'edward']

for name in list:
    if name in favorite_languages.keys():
        print(f"Hello, {name.title()}. Thank you for your response.")
    else:
        print(f"Hello, {name.title()}. It seems you have not taken the poll yet. Please answer the poll. Thank you.")