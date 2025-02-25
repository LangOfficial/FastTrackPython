# 4-4. How Many Teachers Are There?

import math

students = 620
students_per_teacher = 30
teachers = math.ceil(students / students_per_teacher)
print(f"We need {teachers} teachers!")