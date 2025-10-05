#this progam uses the max funtion to determine the max number of two input numbers

def max():

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if num1 > num2:
        print(f'The max is {num1}')
    else:
        print(f'The max is {num2}')

max()