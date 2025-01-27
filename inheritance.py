# intheritance is best when you have 2 similar classes
# so you want remove __init__ and make 


class Animal: # Generalization when classes have sm=imlar things but a couple different things
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display_info(self):
    print(f"I am {self.name}")
    print(f"I am {self.age} years old")
  
  def speak(self):
    print("I don't speak.")

class Cat(Animal): # specific class
  def __init__(self, name, age, color):
    super().__init__(name, age) # super is used to reference the parent class these are the attributes that are passed
    self.color = color
  def speak(self):
    print("Meow")

class Dog(Animal):
  def speak(self): # overwrites parent class cause more specifci to the object
    print("Bark")

p = Dog("Cheese", 19)
#with super, the child classes only take parent's class 
# everything from parent is shared, attributes, methods
p.display_info()
p.speak()