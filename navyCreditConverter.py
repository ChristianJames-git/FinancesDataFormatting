import re

with open('navy_credit.txt', 'r') as f:
    lines = f.readlines()

for line in reversed(lines):
    if "CHASE" in line:
        continue
    if "CITI" in line:
        continue
    if "Credit Card" in line:
        continue

    line = line.strip().replace("\n", "")
    date2, date, location, card, amount, total = line.split("\t")

    if "YouTubePremium" in location:
        location = "YouTube Premium"
    elif "PAYMENT RECEIVED" in location:
        location = "Pay Navy Credit"
        print(f"{date}@{location}@8887@-{amount}")
    elif "Amazon Prime" in location:
        location = "Amazon Prime"
    else:
        location = location.split(" ")[0]

    # Format the output string
    output_string = f"{date}@{location}@{card}@{amount}"

    # Print the result
    print(output_string)