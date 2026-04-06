# Input data
product_name = input("Enter the product name: ")
unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))

# Total price without discount
total_price = unit_price * quantity

# Determine discount
if quantity <= 10:
    discount = 0
elif quantity <= 20:
    discount = total_price * 0.10
elif quantity <= 50:
    discount = total_price * 0.20
else:
    discount = total_price * 0.25

# Final price
final_price = total_price - discount

# Output
print("\nProduct:", product_name)
print("Total price without discount: $", total_price)
print("Final price with discount: $", final_price)