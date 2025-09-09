# Create a program that asks for the user’s name and age, then prints:
# "Hello [name], you will be [age+1] next year!"

name = input("Name: ")
age = input("Age: ")

print(f"What would you like to see {name}?\n")
ask = input("[1] Age next year\n[2] age in x years\n> ")

if ask == '1':
    age_next_year = int(age) + 1
    print(f"Ok {name}, you will be {age_next_year} next year!")
elif ask == '2':
    x_years = input("How many years?\n> ")
    age_in_x_years = int(age) + int(x_years)    
    print(f"Ok {name}, you will be {age_in_x_years} in {x_years} years!")