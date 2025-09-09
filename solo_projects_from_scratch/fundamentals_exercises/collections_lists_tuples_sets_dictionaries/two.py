# Remove duplicates from a list without using set()

import random

def remove_duplicates():
    
    numbers = [random.randint(1, 1000) for _ in range(1, 100)]

    clean = []
    duplicates = []
    
    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
        elif numbers.count(num) == 1:
            clean.append(num)
                   
    print("\nYour numbers:\n", clean, "\n")
    print("Here are your duplicates:\n", duplicates)

def main():
    
    remove_duplicates()


main()


## I completely forgot about the .count() method, but once i found it online i was able 
#  to figure the rest out on my own. the 'and not in duplicates' condition was a correction
#  that chat gpt recommended so that every occurance of the duplicate number
#  didnt appear in the duplicates list, but the prompt didnt specify whether i needed
#  to make that distinction in my solution or not. 