import time, math

a = float(input("Enter the length of leg A: "))
b = float(input("Enter the length of leg B: "))

hypotenuse = math.sqrt(a ** 2 + b ** 2)
 
print("Calculating...") 
time.sleep(.5)
 
print(f"The hypotenuse that forms with legs {a} and {b} is {round(hypotenuse, 1)}")