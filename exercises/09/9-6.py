# 9-6: Membership is Awesome

is_member = True
spending = 120

if is_member or spending > 100:
  print("You get a discount!")
else:
  print("Have a good day!")

# ternary
discount = "You get a discount!" if is_member or spending > 100 else "Have a good day!"
print(discount)

