## Print all numbers 1-100, but replace:
#  - multiples of 3 with "Fizz"
#  - multiples of 5 with "Buzz"
#  - multiples of both with "FizzBuzz"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)