## Create a simple phonebook program using a dictionary:
#  User can add a contact, search for a contact, or delete one

# Create phonebook as a dictionary: name → number
phonebook = {}

# Function to add a contact
def add_contact():
    name = input("\nContact name: ")
    number = input("Contact number: ")
    phonebook[name] = number  # name is the key, number is the value
    print(f"Added {name} to phonebook.")

# Function to search contacts by name OR number
def search_phonebook():
    while True:
        ask = input("\nSearch by:\n[1] Name\n[2] Number\n> ")
        
        if ask == '1':
            name = input("\nContact name: ")
            if name in phonebook:
                print(f"\n{name}: {phonebook[name]}")
            else:
                print("Contact not found.")
            break

        elif ask == '2':
            number = input("\nContact number: ")
            # Since number is the value, we loop through key-value pairs
            found = False
            for name, num in phonebook.items():
                if num == number:
                    print(f"\n📞 {name}: {num}")
                    found = True
                    break
            if not found:
                print("Contact not found.")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")

# Function to remove contact by name or number
def remove_contact():
    while True:
        ask = input("\nRemove by:\n[1] Name\n[2] Number\n> ")
        
        if ask == '1':
            name = input("\nContact name: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted contact {name}.")
            else:
                print("Contact not found.")
            break

        elif ask == '2':
            number = input("\nContact number: ")
            # Find the name that matches the number
            found = False
            for name, num in list(phonebook.items()):  # Use list() to safely modify while iterating
                if num == number:
                    del phonebook[name]
                    print(f"Deleted contact {name}.")
                    found = True
                    break
            if not found:
                print("Contact not found.")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")

# List all contacts
def list_contacts():
    if not phonebook:
        print("\nYour phonebook is empty.\n")
    else:
        print("\nYour contacts:")
        for name, number in phonebook.items():
            print(f"• {name}: {number}")
        print()

# Main program loop
def main():
    while True:
        prompt = input(
            "\nWhat would you like to do?\n"
            "[1] Add contact\n"
            "[2] Remove contact\n"
            "[3] Search phonebook\n"
            "[4] Show contacts\n"
            "[5] Quit\n\n> "
        )

        if prompt == '1':
            add_contact()
        elif prompt == '2':
            remove_contact()
        elif prompt == '3':
            search_phonebook()
        elif prompt == '4':
            list_contacts()
        elif prompt == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()



## I struggled with this one alot and eventually just had to have chatgpt walk me through it.
#  I was able to get the basic skeleton working but i couldn't figure out how to search through the dictionary by number
#  I asked chat gpt to fix my code and explain it to me in depth so i could understand what was working and what wasn't and
#  exactly how to fix it.

## What I leanred:
#  How to search through a dictionary until you find a key with a value matching a specific criteria
#  How to loop through a dictionary (for key, value in dictionary.items():) this allows us to examine both key and value
#  at the same time. Then you can preform your operations based on those iteration variables.
