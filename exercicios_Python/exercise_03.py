print("Video Rental Store")

category = input("Movie category (R/G/S/B): ").upper()
rent_day = int(input("Rental day: "))
expected_return_day = int(input("Expected return day: "))
actual_return_day = int(input("Actual return day: "))

match category:
    case "R":
        category_name = "Release"
        price = 3.00
        daily_fine = 2.00
    case "G":
        category_name = "Gold"
        price = 2.50
        daily_fine = 1.50
    case "S":
        category_name = "Silver"
        price = 2.00
        daily_fine = 1.00
    case "B":
        category_name = "Bronze"
        price = 1.50
        daily_fine = 0.75
    case _:
        print("Invalid category")
        exit()

# Calculate delay
late_days = 0
if actual_return_day > expected_return_day:
    late_days = actual_return_day - expected_return_day

# Calculate fine
fine = late_days * daily_fine

# Total value
total = price + fine

print("\nVideo Rental Store")
print("Category:", category_name)
print("Late days:", late_days)
print("Rental price: $", price)
print("Fine: $", fine)
print("Total: $", total)