# 16-3. People and Employees

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I'm {self.name} and I'm {self.age}.")
      
class Employee(Person):
    def __init__(self, name, age, employee_id):  
      super().__init__(name, age)
      self.name = name
      self.age = age
      self.employee_id = employee_id
    
    def introduce(self):
      print(f"Hello, I'm {self.name} and I'm {self.age}.")
      print(f"My employee ID is {self.employee_id}.")

person = Person("John", 24)
employee = Employee("Jimmy", 19, "S12345")

person.introduce()
employee.introduce()
