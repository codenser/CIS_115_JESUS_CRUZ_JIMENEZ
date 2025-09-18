#this program instructs the user to input up to 10 grades to then print those grades using while loops

#introduce the counter
counter = 0

#allow the user to input up to 10 grades
tenGrades = [10]
#use while loop to enable user to input grades
while counter < 10:
    counter = counter + 1
    grade = int(input("enter your grade: "))

    #print the grade chosen by the user
    print(f"you've registered {grade}.")

    if(counter >= 10):
        print("you have entered 10 grades and are now finished.")