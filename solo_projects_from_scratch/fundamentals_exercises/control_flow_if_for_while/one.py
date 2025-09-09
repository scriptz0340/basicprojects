# Write a program that determines whether a number is odd or even

numbers = [200, 123, 13243, 1223, 34, 23, 5, 6 ,86, 90]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.\n")
    else:
        print(f"{num} is odd.\n")