# 11-9. Popular Items

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}
popular_items = ['pizza']

for food, price in menu.items():
  if food in popular_items:
    print(f"Our famous {food}: ${price}")
  else:
    print(f"{food}: ${price}")