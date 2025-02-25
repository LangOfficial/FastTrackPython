# 13-5. Grocery List

groceries = ['cabbage', 'chips', 'beans', 'bread', 'spaghetti noodles', 'spaghetti sauce', 'ground beef']

for index, grocery in enumerate(groceries, start=1):
  print(f'{index}. {grocery.title()}')