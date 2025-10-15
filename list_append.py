#this program uses the append method to add additional items to a list that will be printed once the user is done

def append_to_list():
    the_list = []
    item = input("Enter item to add to list: ")
    the_list.append(item)

    user = input("Are you done? (y/n): ")

    if user == 'y':
        print(the_list)
    else: user == 'n'
    item = input("enter item to add to list: ")
    the_list.append(item)
    print(the_list)

    

append_to_list()