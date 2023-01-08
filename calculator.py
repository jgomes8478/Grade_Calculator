if __name__ == "__main__":
    # ask for the student's name
    name = input("Enter the student's name: ")

    # ask for the number of subjects
    num_subjects = int(input("Enter the number of subjects: "))

    # initialize a list to store the grades
    grades = []

    # loop through and get the grades for each subject
    for i in range(num_subjects):
        grade = input(f"Enter the grade for subject {i+1}: ")
        grades.append(grade)

    # calculate the GPA
    gpa = 0
    for grade in grades:
        if grade == "A":
            gpa += 4.0
        elif grade == "B":
            gpa += 3.0
        elif grade == "C":
            gpa += 2.0
        elif grade == "D":
            gpa += 1.0
        else:
            gpa += 0.0
    gpa /= num_subjects

    # print the results
    print(f"{name} received {num_subjects} grades with a GPA of {gpa:.2f}")
