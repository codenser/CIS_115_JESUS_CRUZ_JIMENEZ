#this program uses a funtion to calculate theta of a right tringle and prints result in degrees
import math
#to solve for theta we will use the atan2(y,x) function

def caTheta(a, b):
    tRadians = math.atan2(a, b)
    tDegrees = (tRadians * 180) / math.pi
    return tDegrees

sideA = float(input("Enter length of side A: "))
sideB = float(input("Enter length of side B: "))
caTheta = caTheta(sideA, sideB)
print("the angle theta is", caTheta, "degrees")
