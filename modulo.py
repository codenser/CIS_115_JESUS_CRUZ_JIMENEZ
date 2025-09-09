#this program uses the modulo operator to determine if the outcome is even or odd
num1 = input("Enter first number: ")

outcome = int(num1) %  2

if outcome % 2 == 0:
    print(f"Even")
else:
    print(f"Odd")