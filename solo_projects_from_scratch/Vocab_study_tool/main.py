import random

file = 'wordlist.txt'

def import_wordlist():
    with open(file, 'r') as f:
        wordlist = [line.strip() for line in f.readlines()]
    
    return wordlist

def add_word(wordlist):
    add = input("\nAdd a word to your study list: ")
    wordlist.append(add)
    print_list(wordlist)


def remove_word(wordlist):
    while True:
        remove = input("\nRemove a word from your study list: ")
        try:
            if remove in wordlist:
                wordlist.remove(remove)
                print_list(wordlist)
                break
        except:
            print("Word not in list!\n")
            continue

def generate_word(wordlist):
    while True: 
        word = random.choice(wordlist)
        ask = input(f"\nDefine {word}: \n> ")
        if ask == 'skip':
            continue
        else:
            break

def save_list(wordlist):
    with open(file, 'w') as f:
        for line in wordlist:
            f.write(line + '\n')

def print_list(wordlist):
    print("\nHere is your study list: ")
    print(wordlist)

def main():
    
    wordlist = import_wordlist()
    print_list(wordlist)

    while True:
        if len(wordlist) == 0:
            ask = input("Add a word? (y/n)\n> ")
            if ask != 'y':
                save_list(wordlist)
                break
            else:
                add_word(wordlist)
        else:
            ask = input("\n[1] Add word\n[2] Remove word\n[3] Generate word\n(q to quit)\n\n> ")
            if ask == '1':
                add_word(wordlist)
            elif ask == '2':
                remove_word(wordlist)
            elif ask == '3':
                generate_word(wordlist)
            elif ask == 'q':
                save_list(wordlist)
                break
            else:
                print("Invalid choice")



main()


