#This program aloows a user to enter an input number within the range of 1-100

#introduce min and max variables
min = 0
max = 100

#introduce flag for while loop
done = False

while not done:
    nums = int(input("Enter a number between 1 and 100: "))

    if nums >= 1 and nums <= 100:
        print(f"You enter {nums}, which is in the range of 1 and 100.")
        done = True
    else:
        print(f"You'ved entered {nums}, which is out of range, try again.")
