# 9-8. Too Expensive Cars

cars = ['BMW', 'Toyota', 'Ford', 'Ferrari', 'Cadillac', 'Ferrari']
expensive_cars = ['Ferrari', 'BMW']
expensive_car_count = 0

for car in cars:
  if car in expensive_cars:
    expensive_car_count += 1

print(f"There are {expensive_car_count} expensive cars.")