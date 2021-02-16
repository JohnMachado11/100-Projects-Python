# HIGHEST STUDENT SCORES

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


# Method 1
max = student_scores[0]

for i in range(1, len(student_scores)):
    if max < student_scores[i]:
        max = student_scores[i]
    
print(f"The highest score in the class is: {max}")

# Method 2
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")