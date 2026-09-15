import csv
from tariff_analysis import (calculate_flat_rate_bill, calculate_tiered_bill, calculate_saving_suggestion)

total_consumption = 0

with open("sample_usage_data_month.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_consumption += float(row["kWh"])

print(f"Total consumption: {total_consumption:.2f} kWh")


# Flat bill
flat_bill = calculate_flat_rate_bill(total_consumption, rate=0.3, fixed_fee=10)
print(f"Flat-rate bill: ${flat_bill:.2f}")


# Tiers
tiers = [
    (100, 0.20),
    (300, 0.30),
    (500, 0.40)
]

tiered_bill = calculate_tiered_bill(total_consumption, tiers=tiers, fixed_fee=10)
print(f"Tiered bill: ${tiered_bill:.2f}")


# Savings
saving = calculate_saving_suggestion(flat_bill, tiered_bill)

if saving > 0:
    print(f"Potential saving: ${saving:.2f}")
else:
    print(f"The alternative tariff does not save any money.")
    # extra_cost = tiered_bill - flat_bill
    # print(f"The alternative tariff costs ${extra_cost:.2f} more.")