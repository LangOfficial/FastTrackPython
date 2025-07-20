import time

first_number = input("Enter your first number: ")
second_number = input("Enter your second number: ")
operator = input("Enter an operator (+, -, *, /, **, or %): ")

# Don't use eval() in production code due to being able to execute arbitrary code if misused!
# Even if it's non-production code, I highly recommend not using it to avoid it becoming a habit.
result = eval(f"{first_number} {operator} {second_number}") # For learning purposes only

print("Calculating...")
time.sleep(.5) # Takes number in seconds

print(f"{first_number} {operator} {second_number} = {result}")
