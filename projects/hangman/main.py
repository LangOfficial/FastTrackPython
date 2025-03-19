from words import pick_word

print("Welcome to Hangman!")
word = pick_word()
guessed_letters = set()
user_word = ["-"] * len(word)
attempts = 6

while attempts > 0 and ''.join(user_word) != word:
    print(f"\nGuess the {len(word)} word!")
    print(''.join(user_word))
    print(f"Attempts: {attempts}")

    user_letter = input("Enter a letter: ").lower()
    if user_letter in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.add(user_letter)

    if user_letter in word:
        for i in range(len(word)):
            if word[i] == user_letter:
                user_word[i] = user_letter
        print(''.join(user_word))
    else:
        attempts -= 1
        print(f"Incorrect!")
    
if attempts == 0:
  print(f"Game over! The word was {word}")
else:  
  print(f"Congratulations, you guessed the word {word} in {attempts} attempts!")
