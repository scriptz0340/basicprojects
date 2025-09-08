file = 'list.txt'

with open(file, 'r') as f:
    todo = [line.strip() for line in f.readlines()]


def add_task():
    add = input("\nadd task: ")
    todo.append(add)
    print("\nTask added!")

def remove_task():
    remove = input("\nRemove chore: ")
    todo.remove(remove)
    print("\nTask removed!")

def print_todo_list():
    if len(todo) == 0:
        print("\nYour To-do list is empty!")
    else:
        print("\nHere is your to-do list:")
        print(todo)

def save_list():    
    with open(file, 'w') as f:
        for task in todo:
            f.write(task + '\n')

def main():
    
    while True:
        print_todo_list()
        if len(todo) == 0:
            ask = input("Add task? (y/n)\n> ")
            if ask == 'y':
                add_task()
            else:
                save_list()
                break
                                 
        else:
            prompt = input("\n[1] Add task\n[2] Remove task\n(q to quit)\n\n> ")
            if prompt == 'q':
                save_list()
                break
            elif prompt == '1':
                add_task()
            elif prompt == '2':
                remove_task()
            else:
                print("Invalid input.")



main()
                






    



