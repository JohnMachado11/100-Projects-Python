# AVERAGE HEIGHT OF ALL STUDENTS

# Example input = 67 82 51 31 21
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Method 1 - Easy
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)

print(f"Students average height = {average_height}.")
