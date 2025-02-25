# 6-5: One Shark and a School of Fish

group = ["shark", "fish", "fish", "fish"]

group[0] = 'big fish'
print(group)

# could also use .index() if you don't want to assume the position of the shark
# note that this exercise is before displaying .index() with a list but we done it with a string.
group[group.index('shark')] = 'big fish'
print(group)
