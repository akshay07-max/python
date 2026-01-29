Complete Example with Good Comments
Create file: student_grade.py
"""
Student Grade Calculator
Calculates final grade based on assignments, midterm, and final exam.
Author: Your Name
Date: 2024-01-26
"""

print("=== Student Grade Calculator ===\n")

# Get student information
student_name = input("Enter student name: ")

# Get scores (out of 100)
assignment_score = float(input("Enter assignment score (0-100): "))
midterm_score = float(input("Enter midterm score (0-100): "))
final_score = float(input("Enter final exam score (0-100): "))

# Calculate weighted average
# Grading policy: Assignments 30%, Midterm 30%, Final 40%
ASSIGNMENT_WEIGHT = 0.30
MIDTERM_WEIGHT = 0.30
FINAL_WEIGHT = 0.40

final_grade = (
    assignment_score * ASSIGNMENT_WEIGHT +
    midterm_score * MIDTERM_WEIGHT +
    final_score * FINAL_WEIGHT
)

# Determine letter grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
if final_grade >= 90:
    letter_grade = "A"
elif final_grade >= 80:
    letter_grade = "B"
elif final_grade >= 70:
    letter_grade = "C"
elif final_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print(f"\n{'='*40}")
print(f"Student: {student_name}")
print(f"Final Grade: {final_grade:.2f}%")
print(f"Letter Grade: {letter_grade}")
print(f"{'='*40}")