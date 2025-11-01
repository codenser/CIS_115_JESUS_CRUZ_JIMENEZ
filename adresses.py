#this progtam uses user-defined functions to create a dictionary stores names and adresses

#defining the function that will create the dictionary
def print_dictionary():
    names_and_addresses = {}
    names_and_addresses['firstName'] = ['John', 'Jane', 'Jim']
    names_and_addresses['lastName'] = ['Doe', 'Smith', 'Brown']
    names_and_addresses['city'] = ['New York', 'Los Angeles', 'Chicago']
    names_and_addresses['state'] = ['NY', 'CA', 'IL']
    names_and_addresses['zip'] = ['10451', '90001', '60341']
    names_and_addresses['phone'] = ['555-1234', '555-5678', '555-8765']
    return names_and_addresses
#printing the dictionary created by the function
print(print_dictionary()['city'])
