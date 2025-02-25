# 16-1. Pet Class

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

pet.fly()
pet.eat()

wild_bird.fly()
wild_bird.eat()