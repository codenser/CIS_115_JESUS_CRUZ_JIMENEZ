#this program uses a user-defined funtion to print iterations using for loops with a range that accepts the argument val

def print_iterations():
    #this for loop will increment the local variable loopCounter
    val = int(input("enter a value: "))
    for loopCounter in range(val):
        print(f'The function call looped {loopCounter + 1} times')

print_iterations() 



