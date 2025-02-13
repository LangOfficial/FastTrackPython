# 15-4. Car Dealer

class Car:
   number_of_cars = 0
   def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
      Car.number_of_cars += 1

   def display_car_count(self):
      print(Car.number_of_cars)

car1 = Car("Toyota", "Camry", 2020)
car1.display_car_count()
