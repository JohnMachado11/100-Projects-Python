# HIGHEST STUDENT SCORES

# Example input = 67 82 98 67 82
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Method 2 - Harder
max = student_scores[0]

for i in range(1, len(student_scores)):
    if max < student_scores[i]:
        max = student_scores[i]
    
print(f"The highest score in the class is: {max}")