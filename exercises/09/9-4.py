# 9-4 : What Did You Get?

score = int(input("What did you get on the math test? "))

if score >= 90: # A
  print(f"{score}? That's an A. Good job!")
elif score >= 80: # B
  print(f"{score}? That's a B. You did well!")
elif score >= 70: # C
  print(f"{score}? That's a C. At least you passed.")
elif score >= 60: # D
  print(f"{score}? That's a D. That sucks.")
elif score >= 50: # F
  print(f"{score}? That's an F. You failed me.")
else:
  print("Huh?")