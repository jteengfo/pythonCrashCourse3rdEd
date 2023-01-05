'''
Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
'''

numbers = list(range(1,1000001))

min_num = min(numbers)
print(min_num)

max_num = max(numbers)
print(max_num)

print(sum(numbers))