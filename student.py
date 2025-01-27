class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade
  
class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = [] # is an attribute but isnt passed because we want all courses have a list of students

  def add_students(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False
  
  def get_average_grade(self):
    value = 0
    for student in self.students:
      value += student.get_grade()

    return value / len(self.students)

student_1 = Student("Greg", 20, 90)
student_2 = Student("Jimmy", 18, 68)
student_3 = Student("Alyssa", 20, 95)

math_course = Course("Math", 2)
math_course.add_students(student_1)
math_course.add_students(student_2)
print(math_course.students)
