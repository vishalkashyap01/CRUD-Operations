# add task to list - function
# version - 1.0.3

def add(li):
    task = input("write task to add : ")
    li.append(task)
    print("<< ", li, " >>")
    make_list()


# tasks to delete from the list
def remove(li):
    print('\n')
    erase = int(input("\n Enter task no to remove from the list : "))
    li.pop(erase)
    print("<< ", li, " >>")
    make_list()


def make_list():
    choice = int(input("1 for add & 0 for not : "))
    if choice == 1:
        add(todo)
    elif choice == 0:
        for a in todo:
            print(a)
        remove(todo)
    else:
        return


# main method
todo = []

print("Are you want to make a todo list -->")
make_list()

for i in range(0, 4):
    print(i+1, '. ', todo[i])
make_list()

for i in range(0, 4):
    print(i, '. ', todo[i])
