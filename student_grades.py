#this program will use a user-defined function to creat a dictonary that stores their names as the key and grade as the value



#add inputs into the student_grades disctonary
def calculate_student_grade():

#implement the empty dictonary
    student_grades = {}
    add_student = True
    while add_student:
        student_name = input("enter name:")
        student_grade = float(input("enter grade: "))
        student_grades[student_name] = student_grade
        add_another = input("add another student? (yes/no: ")
        if add_another == "no":
            add_student = False
        else:
            add_student = True
#calculate the average grade of the students
    total = 0
    for grade in student_grades.values():
        total += grade
        average = total / len(student_grades)
        return average
    print(f"the average grade is: {average:.2f}")


#call the function to display the average grade
print(f"The average grade is: {calculate_student_grade():.2f}")
