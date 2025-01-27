class Person:
  number_of_people = 0 # class attributre ebcause it is not connencted to self 
  #remember that self references the object. this is specific to the entire class 
  GRAVITY = -9.8 #better than global variables since you would import classes
  def __init__(self, name): 
    self.name = name
    Person.number_of_people += 1 # when an object get created this will also run 
# only references the class and use on object it no work
Person.number_of_people += 1
print(Person.number_of_people)