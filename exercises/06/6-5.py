# 6-5: One Shark and a School of Fish

group = ["shark", "fish", "fish", "fish"]

group[0] = 'big fish'
print(group)

# Could also use .index() if you don't want to assume the position of the shark
# Note that this exercise is given before showcasing .index() with a list but we done it with a string.
group[group.index('shark')] = 'big fish'
print(group)

