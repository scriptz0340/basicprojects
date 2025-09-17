# Count the frequency of each word in a sentence and store results in a dictionary

sentence = "This is a test. This test is only a test."

words = sentence.split()

word_count = {}

for w in words:
    w = w.lower().strip(".")
    if w not in word_count:        
        word_count[w] = 1
    else:
        word_count[w] += 1

print(word_count)


## so for this one i had to refer to the internet to learn how to store things in a dictionary, as well as learn how to
#  split a string up into words. I sent my first few tries to chat cpt and specifically asked it not to give me 
#  any answers instead guide me and make me figure it out on my own and eventually i got it. 