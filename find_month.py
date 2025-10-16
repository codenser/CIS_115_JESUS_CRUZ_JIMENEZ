#this program uses a user-defined function to find a month and validate whether it was found in the list or not

def search():
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month = input("enter a month: ")
    if month in months:
        print(f"We found {month} in the months list. Search successful!.")
    else:
        print(f'The month {month} was not found in the months list. Search unsuccessful!.')

search()