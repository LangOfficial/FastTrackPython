# 7-1. Hobbies 2

hobbies = ['coding', 'reading', 'tennis', 'lifting weights']

for i in range(4):
  print(hobbies[i])

# bonus
for i in range(len(hobbies)):
  print(f"{i + 1}. {hobbies[i].title()}")