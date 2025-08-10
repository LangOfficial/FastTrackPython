# 9-7: Skip the Exam

grade_letter = 'A'
avg_test_score = 88

if grade_letter == 'A' and avg_test_score >= 85:
  print("You can skip the exam!")
else:
  print("Good luck!")

# ternary
skip_final = "You can skip the exam!" if grade_letter == 'A' and avg_test_score >= 85 else "Good luck!"
print(skip_final)
