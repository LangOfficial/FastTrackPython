# 14-6. Destinations 3

ratings = {"Wendy's": [8, 7, 4], "Knotts Berry Farm": [6, 9, 8], "Taco Bell": [5, 7, 6]}

# manual method example
dest_1 = round(sum(ratings["Wendy's"]) / 3, 1)
dest_2 = round(sum(ratings["Knotts Berry Farm"]) / 3, 1)
dest_3 = round(sum(ratings["Taco Bell"]) / 3, 1)

if dest_1 > dest_2 and dest_1 > dest_3:
  print(f"Wendy's has the highest rating of {dest_1}.")
elif dest_2 > dest_1 and dest_2 > dest_3:
  print(f"Knotts Berry Farm has the highest rating of {dest_2}.")
elif dest_3 > dest_1 and dest_3 > dest_2:
  print(f"Taco Bell has the highest rating of {dest_3}.")

# list comprehension method sample, definitely a lot of ways to do it.
# example is probably overdoing it but it demonstrates a lot of what we learned :)
avg_ratings = [round(sum(x) / len(x), 1) for x in ratings.values()]
highest_rating = max(avg_ratings)
best_index = avg_ratings.index(highest_rating)
best_dest = list(ratings.keys())[best_index]

print(f"{best_dest} has the highest rating of {highest_rating}.")

# loop and variable method
best_dest, highest_rating = "", 0

for dest, ratings in ratings.items():
  total_rating = sum(ratings)
  average_rating = round(total_rating / len(ratings), 1)
  if average_rating > highest_rating:
    highest_rating = average_rating
    best_dest = dest

print(f"{best_dest} has the highest rating of {highest_rating}.")