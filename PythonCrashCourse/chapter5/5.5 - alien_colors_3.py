'''
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

# runs if block
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")

# runs elif yellow block

alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")

# runs elif red block

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")
