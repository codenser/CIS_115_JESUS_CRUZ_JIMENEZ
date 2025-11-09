#this program will break down the process of the mod 10 check using user-defined functions and loops

#create function that will accept the argument ccNum
def validateCreditCard():
    #create empty list to store digits
    ccNum = input("Please enter a credit card number to validate: ")
    #use ccNum input to store value
    for digit in ccNum:
        #reverse the list of digits
        digitsreversed = ccNum[::-1]
        #nummbers will be seperated by even or odd
        odddigits = digitsreversed[0::2]
        evendigits = digitsreversed[1::2]
        #multiply every other digit by 2
    evendigits = [int(digit) * 2 for digit in evendigits]

        #if result is greater than 9, subtract 9
    evendigits = [digit - 9 if digit > 9 else digit for digit in evendigits]

    #sum all the digits
    total = sum(int(digit) for digit in odddigits) + sum(evendigits)

    #if total mod 10 is 0, the number is valid
    if total % 10 == 0:
        print("Credit card number is valid.")
    else:
        print("Invalid credit card entered. Please try again.")
    return validateCreditCard()

validateCreditCard()