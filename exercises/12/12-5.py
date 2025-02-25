# 12-5. Vacation Trip

def vacation_trip(destination, friend):
  print(f"Me and {friend} are going to {destination}!")

# positional
vacation_trip("Paris, France", "Jimmy")

# keyword
vacation_trip(friend="Jimmy", destination="Paris, France")

# mixed
vacation_trip("Paris, France", friend="Jimmy")