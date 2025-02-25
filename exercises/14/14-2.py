# 14-2. Students Only

students = [40, 16, 32, 13, 17, 2, 18]
students = [student for student in students if student <= 18 and student >= 13]

print(students)