# Swap two numbers without using a third variable.

# my idea
numbers = [100, 5]

print(numbers)

print(numbers[::-1])


# Chat gpt correction
a = 23
b = 40

a, b = b, a

print(a, b)

# i didn't know you could use the '=' that way with two variables at once. Also to me it
# still seems like 3 variables but i guess i see how it isn't. If i understand it 
# correctly, then its literally just referncing a specific order
# of 2 variables and saying reverse the change the order. 