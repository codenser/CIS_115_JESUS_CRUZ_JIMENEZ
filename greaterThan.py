# this program uses math and uses if-else statements and division to see if if the outcome is greater than zero

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter divisor: ")

outcome = (float(num1) + float(num2)) / float(num3)
if outcome > 0:
    print("the mathematical operation is > 0")
else:
    print("the mathematical operation is <= 0")

print(outcome)