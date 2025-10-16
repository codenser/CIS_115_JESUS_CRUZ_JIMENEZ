#this program uses the append method to add additional items to a list that will be printed once the user is done

def append_to_list():
    the_list = []
    item = input("Enter item to add to list: ")
    the_list.append(item)

    user = input("Are you done? (y/n): ")

    while user == 'y':
        print(the_list)
    if user == 'n':
        item = input("Enter item to add to list: ")
        the_list.append(item)
    print(the_list)

    

append_to_list()