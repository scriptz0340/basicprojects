# Given a list of numbers, print the largest, smallest, and average

import random

numbers = [random.randint(1, 1000) for _ in range(1, 100)]

print(numbers)
print()
print("The largest number in your list: ", max(numbers))
print("The smallest number in your list: ", min(numbers))
print("The average of all numbers in your list: ", sum(numbers) / len(numbers))
