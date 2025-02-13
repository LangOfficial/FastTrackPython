# 8-3: Even or Odd?

number = int(input("Enter a number: "))

if number % 2 == 0:
  print(f'{number} is even.')
else:
  print(f'{number} is odd.')

# ternary
even_odd = 'even' if number % 2 == 0 else 'odd'
print(f'{number} is {even_odd}.')