#this progam uses a user-defined function to calculate the hypotenuse of a right triangle
import math #importing this library allows the use of the sqrt function

def calcHypo(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
sideA = float(input("Enter length for side A: "))
sideB = float(input("Enter length for side b: "))
hypotonuse = calcHypo(sideA, sideB)
print("The length of the hypotenuse is", hypotonuse)
