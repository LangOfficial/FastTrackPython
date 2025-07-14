# 10-4. Free Money

grades = ['A', 'B', 'A', 'C', 'B', 'A', 'A']
grades_a = 0

for grade in grades:
    grades_a += 1
    if grade != 'A':
        # They won't know you didn't get an A :)
        continue
    print("You got an A!")

if grades_a == len(grades): # Checker that you did it right.
    print("Here's $1,000 for your hard work!")
