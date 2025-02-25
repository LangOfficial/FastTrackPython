# 11-7. Menu Availability

menu = {"burger": 7.99, "pizza": 9.99, "cookie": 1.25}

# don't necessarily need to have customer dialogue :)
print("Customer: Do you guys have the pizza?")

if 'pizza' in menu:
  print("Yes, we have pizza!")
else:
  print("No, we don't have pizza.")

print("Customer: What about meatball subs?")

if 'meatball subs' in menu:
  print("Yes, we have meatball subs!")
else:
  print("No, we don't have meatball subs.")