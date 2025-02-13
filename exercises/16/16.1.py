# 16-1. Out of Bounds

foods = ['bananas', 'oreos', 'donuts']

try:
  print(foods[3])
except IndexError:
  print("Index out of bounds.")
except:
  print("An error occurred.")

# try:
#   print(foods[3])
# except:
#   print("An error occurred.")
