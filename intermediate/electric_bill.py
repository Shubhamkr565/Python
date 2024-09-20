def electric_bill(unit):
    if unit < 100:
        amount = 5 * unit
    elif unit < 500:  # No need to check for unit >= 100 here
        amount = 8 * unit
    else:
        amount = 10 * unit
    return amount

total_unit = int(input("Enter electric bill unit: "))

# Adding a fixed service charge of 80
service_charge = 80

amount = electric_bill(total_unit)
print(f"Total amount is {amount + service_charge}")
