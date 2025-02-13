# 11-7. Vacation Trip 2

def vacation_trip(destination, *people):
  # print(f"Me and {people} are going to {destination}!") # This is fine but looping would look nicer.
  # print(f"Me and {', '.join(people)} are going to {destination}!") # This is nice but this is beyond what I expect lol. 

  for person in people:
    print(f"Me and {person} are going to {destination}!")

vacation_trip("Tokyo, Japan", "Jimmy", "Timmy", "Alyssa")