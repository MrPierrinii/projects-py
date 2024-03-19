# Week 5 Assignment 
# CMIS Introduction to Problem solving and Algorithm 
# This program prompts the user for three grades for each of four students,
# calculates the weighted average grade for each student, and determines which
# student has the highest grade.

# Define a function to calculate the weighted average grade for a student
def calculate_weighted_average_grade(student_name):
    # Prompt the user for the three grades for the student
    discussion_grade = float(input("Enter the discussion grade for " + student_name + ": "))
    quiz_grade = float(input("Enter the quiz grade for " + student_name + ": "))
    assignment_grade = float(input("Enter the programming assignment grade for " + student_name + ": "))

    # Calculate the weighted average grade using the given formula
    wtAvgGrade = discussion_grade * 0.15 + quiz_grade * 0.35 + assignment_grade * 0.5

    # Return the calculated average
    return wtAvgGrade

# Define a list of four student names
student_names = ["Alice", "Bob", "Charlie", "Cedrick Pierre"]

# Initialize the highest average grade to zero and the name of the student with
# the highest grade to an empty string
highest_grade = 0.0
highest_grade_student = ""

# Loop over each student name in the list
for student_name in student_names:
    # Calculate the weighted average grade for the student
    wtAvgGrade = calculate_weighted_average_grade(student_name)

    # Check if this student's grade is the highest so far
    if wtAvgGrade > highest_grade:
        highest_grade = wtAvgGrade
        highest_grade_student = student_name

    # Display the calculated average grade for the student
    print(student_name + "'s weighted average grade is:", wtAvgGrade)

# Display the name of the student with the highest grade
print("The student with the highest grade is:", highest_grade_student)
print("Their grade is:", highest_grade)
