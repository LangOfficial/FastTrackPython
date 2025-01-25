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

def add_card(question, answer):
    flashcards[question] = answer
    print("New card added!")
    
def review_cards():
    for question, answer in flashcards.items():
        print(question)
        input("Hit 'enter' to reveal the answer.")
        print(answer)

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
        pass
    elif option == 4:
        pass
    elif option == 5:
        print("Exiting the program...")
        break
    else:
        print("Invalid option!")
        continue