# AVERAGE HEIGHT OF ALL STUDENTS

# Example input = 67 82 51 31 21
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Method 2 - Harder
num_students = 0
total_height = 0 

for i in range(0, len(student_heights)):
    total_height += student_heights[i]
    num_students += 1

avg = round(total_height / num_students)
print(f"Students average height = {avg}.")
