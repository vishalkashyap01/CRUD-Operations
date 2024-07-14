# Version 1.0.5 - Todo List Manager

# Function to add a task to the todo list
def add_task(todo_list):
    task = input("Write task to add: ")
    todo_list.append(task)
    print("<< Updated list: ", todo_list, " >>")
    make_list(todo_list)

# Function to remove a task from the todo list
def remove_task(todo_list):
    print('\n')
    erase = int(input("\nEnter task number to remove from the list: "))
    if erase < len(todo_list):
        todo_list.pop(erase)
        print("<< Updated list: ", todo_list, " >>")
    else:
        print("Invalid task number.")
    make_list(todo_list)

# Function to update a task in the todo list
def update_task(todo_list):
    print('\n')
    task_no = int(input("\nEnter task number to update: "))
    if task_no < len(todo_list):
        new_task = input("Enter new task: ")
        todo_list[task_no] = new_task
        print("<< Updated list: ", todo_list, " >>")
    else:
        print("Invalid task number.")
    make_list(todo_list)

# Function to view tasks in the todo list
def view_tasks(todo_list):
    print('\n')
    if not todo_list:
        print("Todo list is empty.")
    else:
        print("<< Current todo list: ", todo_list, " >>")
    make_list(todo_list)

# Function to display the menu and handle user input
def make_list(todo_list):
    print('\n')
    print("Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Update a task")
    print("4. View tasks")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task(todo_list)
    elif choice == 2:
        remove_task(todo_list)
    elif choice == 3:
        update_task(todo_list)
    elif choice == 4:
        view_tasks(todo_list)
    elif choice == 0:
        print("\nExiting...")
        return
    else:
        print("\nInvalid choice.")
        make_list(todo_list)


# Main method to initialize todo list and start the application
if __name__ == "__main__":
    todo_list = []

    print("Do you want to create a todo list?")
    make_list(todo_list)

# Author - vishalkashyap01
