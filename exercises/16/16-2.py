# 16-2. New Pets

class Bird:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def fly(self):
        print(f"{self.name} the {self.age}-year-old {self.breed} is flying.")  

    def eat(self):
        print(f"{self.name} the {self.breed} is eating.") 

pet = Bird('Cheese', 12, 'Parakeet')
wild_bird = Bird('Pecky', 1, 'Sparrow')

pet.name = "Queso"
print(pet.name)
print(pet.age)
print(pet.breed)

wild_bird.age = 2
wild_bird.fly() # using .fly() to see age