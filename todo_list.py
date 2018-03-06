# make a list that will hold onto items

todo_list = []

# print out instructions on how to use app

print("What do you want to get done today?")

def show_help():
    print("""
Enter 'HELP' for more options
Enter 'SHOW' to see your current list
Enter 'DONE' when you are finished adding items
""")

show_help()

def show_list():
    # print out the list
    for item in todo_list:
        print(item)

def add_to_list(new_item):
    # add new items to list
    todo_list.append(new_item)
    print("{} added. You now have {} things to do today.".format(new_item, len(todo_list)))

while True:
    # ask for new items
    # able to quit the app
    new_item = input("> ")
    if new_item == "DONE":
        break
    if new_item == "SHOW":
        show_list()
        print("""
Is there anything else you want to get done?""")
        continue
    if new_item == "HELP":
        show_help()
        continue
    add_to_list(new_item)

print("""You're going to kill it today! Here's your to-do list:
""")
show_list()
