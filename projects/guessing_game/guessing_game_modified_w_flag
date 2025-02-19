import random
change_range = input("Want to change the range? (y/n) ")
start = 1
end = 10

if change_range == 'y':
    start = int(input("Enter a start: "))
    end = int(input("Enter an end: "))
    
number = random.randint(start, end)
guess = 0
attempts = 5
quitted = False

while number != guess and attempts > 0 and not quitted:
    guess = input(f"Guess a number between {start} and {end}!\nEnter 'q' to quit the game.\n# of attempts: {attempts}\n")
    if guess == 'q':
        # the most simple solution is...
        # could keep it as a break statement, keep "guess == 'q'" an independent if statment  and remove the loop's third condition
        # should be back to "while number != guess and attempts > 0"
        quitted = True
    elif guess.isdigit():
        guess = int(guess)
        if guess > end or guess < start:
            print("Enter a number within the range please!")
            continue
        if guess > number:
            print(f"{guess} is too high!")
        elif guess < number:
            print(f"{guess} is too low!")
        attempts -= 1
    else:
        print("Enter an integer please!")
        continue
if quitted:
    print(f"You quitted the game. The number was {number}.")
elif number != guess and attempts == 0:
    print(f"You ran out of attempts! The number was {number}.")
else:
    print(f"Congratulations, you guessed {number} with {attempts} attempts remaining!")
