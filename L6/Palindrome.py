#this program uses a user defined funtion to determine whether a word is a palindrome or not
def is_palindrome():
    inputString = input("enter text to check if word entered is a palindrome: ")
    reversedString = inputString[::-1]
    if inputString == reversedString:
        print(f'The string {reversedString} is a palindrome')
    else:
        print(f"The string {reversedString} is not a palindrome")
    
is_palindrome()