'''
 All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods
'''

# from foods.py

my_food = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_food[:]

for food in my_food:
    print(food.title())

for food in friend_foods:
    print(food.title())