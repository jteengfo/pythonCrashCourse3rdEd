# changing guest list 
# you just heard that one of your guests can't make the dinner, so you
# need to send out a new set of invitations. Youl'll have to 
# think of someone else to invite. 

# start with you program from 3.4 add a print() call at the end of your program, stating the name of the guest who can't make it

# modify your list, replacing the name of the guest who cant make it with the name of the new person you are inviting 

# print  a second set of invitation messages, one for each person who is still in your list 


invited_people = ["emma watson", 'gal gadot', 'christina ricci']

print(f"Unfortunately, it seems that {invited_people.pop(1).title()} will not be able to make it to dinner.")

invited_people.append("angelina jolie")

print(f"Hello, {invited_people.pop().title()}, you are invited to a bountiful dinner with me!")
print(f"Hello, {invited_people.pop().title()}, you are invited to a bountiful dinner with me!")
print(f"Hello, {invited_people.pop().title()}, you are invited to a bountiful dinner with me!")