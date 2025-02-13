# 16-2. Math Calculators

import math, time

# basic cal

try:
  first_number = float(input("Enter your first number: "))
  second_number = float(input("Enter your second number: "))
except ValueError:
  print("Please enter a number.")
  exit() # ends program
except:
  print("Something unexpected happened. Please try again.")
  exit()

operator = input("Enter an operator (+, -, *, /, **, or %): ")

result = eval(f"{first_number} {operator} {second_number}")

print("Calculating...")
time.sleep(.5) # takes num in seconds

print(f"{first_number} {operator} {second_number} = {result}")

# hypotenuse calc
def get_number_input(prompt): 
    """Continuously ask the user until they enter a number"""
    # had to individually check for each input because if we had multiple inputs being checked and one gets excepted, the user has to start over
    # ex: they typed a word in the 2nd input and the while loop restarts since it didn't end. That makes the user start back at the 1st input
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Get both inputs separately
a = get_number_input("Enter the length of leg A: ")
b = get_number_input("Enter the length of leg B: ")

hypotenuse = math.sqrt(a ** 2 + b ** 2)
 
print("Calculating...") 
time.sleep(.5)
 
print(f"The hypotenuse that forms with legs {a} and {b} is {round(hypotenuse, 1)}")