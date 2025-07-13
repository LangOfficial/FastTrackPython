# 9-2. Is It Lowercase?

word = input('Enter a word: ')

# method way
if word.islower():
  print(f'{word} is in lowercase.')
else:
  print(f'{word} is not in lowercase.')

# == to lowercase string way
if word.lower() == word:
  print(f'{word} is in lowercase.')
else:
  print(f'{word} is not in lowercase.')

# ternary
is_lower = f'{word} is in lowercase' if word.islower() else f'{word} is not in lowercase'
print(is_lower)

