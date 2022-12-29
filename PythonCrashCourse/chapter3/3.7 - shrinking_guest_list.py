'''
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

    Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
    Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
    Print a message to each of the two people still on your list, letting them know they’re still invited.
    Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
'''


invited_people = ["emma watson", 'gal gadot', 'christina ricci']

invited_people.insert(0, "angelina jolie")
invited_people.insert(2, "wendy")
invited_people.append("irene")

print(f"I apologize but the dinner table won't be arriving on time. As a result, I am only able to bring in two guests for the dinner.")

popped_person = invited_people.pop()
print(f"I am sorry, {popped_person.title()}, I will not be able to take you to dinner.")
popped_person = invited_people.pop()
print(f"I am sorry, {popped_person.title()}, I will not be able to take you to dinner.")
popped_person = invited_people.pop()
print(f"I am sorry, {popped_person.title()}, I will not be able to take you to dinner.")
popped_person = invited_people.pop()
print(f"I am sorry, {popped_person.title()}, I will not be able to take you to dinner.")

print(f"Hello, {invited_people[0].title()}, you are still invited to dinner and I look forward to seeing you.")
print(f"Hello, {invited_people[1].title()}, you are still invited to dinner and I look forward to seeing you.")

del invited_people[0]
del invited_people[0]