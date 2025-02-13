# 7-3 : Factorial 10

import math

res = []

for i in range(1, 11):
  fact = math.factorial(i)
  res.append(fact)

print(res)