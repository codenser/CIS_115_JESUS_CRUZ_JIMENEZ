#this program uses a user-defined function to reverse a string input by the user
def reverseMyString():
    inputString = input("enter text to be reversed: ")
    reversedString = inputString[::-1]
    return reversedString

print(reverseMyString())