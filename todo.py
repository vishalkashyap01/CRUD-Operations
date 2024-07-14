# version - 1.0.4

def add(li):
    task = input("Write task to add: ")
    li.append(task)
    print("<< ", li, " >>")
    make_list()

def remove(li):
    print('\n')
    erase = int(input("\nEnter task number to remove from the list: "))
    if erase < len(li):
        li.pop(erase)
        print("<< ", li, " >>")
    else:
        print("Invalid task number.")
    make_list()

def update(li):
    print('\n')
    task_no = int(input("\nEnter task number to update: "))
    if task_no < len(li):
        new_task = input("Enter new task: ")
        li[task_no] = new_task
        print("<< Updated list: ", li, " >>")
    else:
        print("Invalid task number.")
    make_list()

def make_list():
    choice = int(input("\n1 to add, 2 to remove, 3 to update, 0 to exit: "))
    if choice == 1:
        add(todo)
    elif choice == 2:
        remove(todo)
    elif choice == 3:
        update(todo)
    elif choice == 0:
        print("\nExiting...")
        return
    else:
        print("\nInvalid choice.")
        make_list()

# main method
todo = []

print("Do you want to create a todo list?")
make_list()
