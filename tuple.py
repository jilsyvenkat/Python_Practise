# TODO: Create a nested tuple of student names and their grades

student_grades = (("Jil", 85), ("Wil", 78), ("Adi", 92), ("Mark", 80), ("Sam", 76))

# TODO: Merge it with an additional nested tuple containing other students' grades

new_student_grades = student_grades + (("Ven", 85),)

# TODO: Print the combined tuple

print(new_student_grades)

# TODO: Check if a student named "Mark" with a grade of "80" is in the combined tuple
print((("Mark", 80)) in new_student_grades)