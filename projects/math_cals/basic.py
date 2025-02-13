import time

first_number = input("Enter your first number: ")
second_number = input("Enter your second number: ")
operator = input("Enter an operator (+, -, *, /, **, or %): ")

result = eval(f"{first_number} {operator} {second_number}")

print("Calculating...")
time.sleep(.5) # takes num in seconds

print(f"{first_number} {operator} {second_number} = {result}")