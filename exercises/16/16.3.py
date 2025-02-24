# 16-3. Are You Old Enough to Drive?

def check_driving_age(age):
    if age < 16:
        raise ValueError("You're too young to drive!")
    return "You're old enough to drive!"
    
print(check_driving_age(10)) # Raises ValueError
print(check_driving_age(19))
