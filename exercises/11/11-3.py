# 11-3. Limited Time Items

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}

print("Limited items here...")

menu["hot cheeto stuffed lobster"] = 40.99
menu["heart shaped cookie"] = 1.50

print(menu)

print("One month later...")

menu.pop('hot cheeto stuffed lobster')
menu.pop('heart shaped cookie')

print(menu)