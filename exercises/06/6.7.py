# 6-7. Students Scores

scores = [90, 84, 29, 94, 56]

# .sort and .reverse (expected solution)
scores.sort() # ascending order
print(scores)

scores.reverse() # make it descending
print(scores)

# introduced after exercise

# using .sort(reverse=True)

# using sorted()
print(sorted(scores))
print(sorted(scores, reverse=True))