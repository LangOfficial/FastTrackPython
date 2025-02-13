# 9-5: Serving Customers

customers = ['Jimmy', 'Timmy']

while customers:
  print("There's customers!")
  customer = customers.pop(0)
  print(f"Serving customer {customer}...")
  print("Customer has been served.")
  is_new_customer = input("Do you see a new customer? (y/n) ")
  if is_new_customer.lower() == 'y':
    new_customer = input("Enter the new customer's name: ")
    customers.append(new_customer)

print("No more customers!")
