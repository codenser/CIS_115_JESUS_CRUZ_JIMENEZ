#this program subtracts two numbers and determines if the outcome is less than zero
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

diff = int(num1) - int(num2)
if diff < 0:
    print("####################################")
    print("                                    ")
    print("Invalid! The value is less than zero")
    print("                                    ")
    print("####################################")
else:
    print("The values entered were valid integers")