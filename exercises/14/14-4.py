# 14-4. Passing Grade

import random

def determine_pass(scores):
  return ['Pass' if score >= 70 else 'Fail' for score in scores]

scores = [random.randint(30, 100) for _ in range(7)] # bonus: using _ is a naming convention for loop variables that aren't used
# could also predefine scores

print(scores)
print(determine_pass(scores))

