
student_heights = input("Input a list of student heights: ").split()
for i in range(0, len(student_heights)):
    (student_heights[i]) = int(student_heights[i])

total_heights = 0
for heights in student_heights:
    total_heights += int(heights)
average = round(total_heights / (i + 1))
print(average)


