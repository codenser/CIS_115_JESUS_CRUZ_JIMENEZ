#this program uses a user-defined function to call another funtion

def print_message1():
    print("I was called first!")
    def print_message2():
        print("I was called from print_message1()")    
    print_message2()
    
print_message1()