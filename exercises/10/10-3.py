# 10-3: Cart Total

sub_total = 0
tax = .0725 # If you want to apply sale tax (California's sales tax as of 2025)

while True:
  price = input("Enter a price (or 'done' to finish): ")
  if price.lower() == "done":
    break
  sub_total += float(price)

total = round(sub_total + sub_total * tax, 2)
print(f"Your total is ${total}.")
