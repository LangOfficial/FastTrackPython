class Person: #CamelCase
  def __init__(self, name, age): # init is the attribute creator and when it object gets created, it runs 
    self.name = name
    self.age = age

  def introduce(self): # method is function in a class
    print(f"Hi, I'm {self.name} and I'm {self.age} years old!")
  def set_age(self, age):
    self.age = age

  def walk(self):
    return "walk"
# the reason we use classes is you could define infinte objects has similar benefits like functions
person = Person("Langli", 17) # object of the class
person2 = Person("Greg", 28)
person.set_age(18)
print(person.age)
# self references the object
print(person.walk())