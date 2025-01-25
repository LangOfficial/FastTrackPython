import random

number = random.randint(1, 10)
guess = 0
attempts = 0

while number != guess:
    guess = input(f"Guess a number between 1 and 10!\nEnter 'q' to quit the game\n# of attempts: {attempts}\n")
    if guess == "q":
        break
    if guess.isdigit():
        guess = int(guess)
        if guess > 10 or guess < 1:
            print("Enter a number within the range please!")
            continue
        if guess > number:
            print(f"{guess} is too high!")
        elif guess < number:
            print(f"{guess} is too low!")
        attempts += 1
    else:
        print("Enter an integer please!")
        continue
    
print(f"Congratulations, you guessed {number} in {attempts} attempts!")
