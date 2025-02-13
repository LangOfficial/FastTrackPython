# 9-3: Cart Total

sub_total = 0
tax = .0725 # if you want to apply tax

while True:
  price = input("Enter a price (or 'done' to finish): ")
  if price.lower() == "done":
    break
  sub_total += float(price)

total = round(sub_total + sub_total * tax, 2)
print(f"Your total is ${total}.")