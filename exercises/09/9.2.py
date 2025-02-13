# 9-2: User Countdown

countdown = int(input("Enter a countdown number: "))

while countdown < 0:
  print("Invalid countdown number. Please enter a non-negative number.")
  countdown = int(input("Enter a countdown number: "))

while countdown > 0:
  print(countdown)
  countdown -= 1

print("Countdown complete!")