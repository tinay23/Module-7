# Student Grade Management System

# Student information variables
student_name = "John Doe"  # String variable representing the student's name
student_age = 18  # Integer variable representing the student's age
student_grades = [85, 90, 78, 92]  # List variable representing the student's grades

# Function to calculate the average grade
def calculate_average_grade(grades):
    """
    Calculates the average grade based on a list of grades.
    Returns the average grade.
    """
    total = sum(grades)
    average = total / len(grades)
    return average

# Function to determine the grade status
def get_grade_status(average_grade):
    """
    Determines the grade status based on the average grade.
    Returns a string indicating the grade status.
    """
    if average_grade >= 90:
        return "Excellent"
    elif average_grade >= 80:
        return "Good"
    elif average_grade >= 70:
        return "Average"
    else:
        return "Below Average"

# Function to display the student's grades
def display_grades(grades):
    """
    Displays each grade from the given list.
    """
    for i, grade in enumerate(grades, start=1):
        print("Subject", i, "Grade:", grade)

# Calculate the average grade
average_grade = calculate_average_grade(student_grades)

# Get the grade status
grade_status = get_grade_status(average_grade)

# Display the student's information and grades
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Average Grade:", average_grade)
print("Grade Status:", grade_status)
print("Grades:")
display_grades(student_grades)

# Section explanations
# The calculate_average_grade function calculates the average grade based on a list of grades.
# The get_grade_status function determines the grade status based on the average grade.
# The display_grades function prints each grade from the given list.
# The program uses these functions to calculate the average grade, determine the grade status,
# and display the student's information and grades.

