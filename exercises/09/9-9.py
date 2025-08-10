# 9-9: Alien Invasion

alien_colors = ['green', 'red', 'yellow', 'red', 'yellow', 'green']

for alien_color in alien_colors:
  if alien_color == 'green':
    print("Hello!")
  elif alien_color == 'yellow':
    print("We should keep an eye on this one.")
  elif alien_color == 'red':
    print("Shoot it down!")
  # else:
  #   print("Shoot it down!")
  # An else statement is fine for this scenario, but if we want to focus on the three types of aliens, it's better to specify them.
  # else can also be used to specifically anything but a green, yellow, or red alien.
  
