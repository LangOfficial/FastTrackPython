flashcards = {
    "What keyword defines a function in Python?": "def",
    "What stores data in programming?": "Variable",
    "What is an ordered collection of items in Python?": "List",
    "What stores key-value pairs in Python?": "Dictionary",
    "What repeats instructions in programming?": "Loop",
    "What compares two values in Python?": "==",
    "What brings external code into Python?": "import",
    "What sends a value back from a function?": "return",
}
tough_cards = {}

def add_card(question, answer):
    flashcards[question] = answer
    print("New card added!")
    
def review_cards():
    for question, answer in flashcards.items():
        print(question)
        input("Hit 'enter' to reveal the answer.")
        print(answer)
        
def mastery_test():
    total = len(flashcards)
    correct = 0
    print("Enter 'q' to quit.")
    for question, answer in flashcards.items():
        print(question)
        user_answer = input("Answer: ")
        if user_answer == 'q':
            break
        if answer.lower() == user_answer.lower():
            print(f"That's right! {answer} is correct!")
            correct += 1
        else:
            tough_cards[question] = answer
            print(f"You'll get it next time. The correct answer is {answer}.")
            
    print(f"You got {correct} correct out of {total}!")

def review_tough_cards():
    # if not tough_cards:
    #     print("No challenging cards found. You're good to go!")
    #     return
    while tough_cards:
        print("Enter 'q' to quit.")
        for question, answer in list(tough_cards.items()):
            print(question)
            user_answer = input("Answer: ") 
            if user_answer == 'q': 
                break
            if answer.lower() == user_answer.lower():
                tough_cards.pop(question)
                print(f"You're improving already! The answer is {answer}!")
            else:
                print(f"Not quite! The answer is {answer}.")
    print("No challenging cards found. You're good to go!")
        # if not tough_cards:
        #     print("No challenging cards found. You're good to go!")
        #     break
            
while True:
    print("\nPython 101 Flashcards\n")
    print("1. Add New Cards")
    print("2. Review Cards")
    print("3. Test for Mastery")
    print("4. Review Toughest Cards")
    print("5. Take a break")
    
    option = int(input("\nWhat would you like to do? "))
   
    if option == 1:
        question = input("Enter question: ")
        answer = input("Enter answer: ")
        add_card(question, answer)
    elif option == 2:
        review_cards()
    elif option == 3:
        mastery_test()
    elif option == 4:
        review_tough_cards()
    elif option == 5:
        print("Exiting the program...")
        break
    else:
        print("Invalid option!")
        continue
