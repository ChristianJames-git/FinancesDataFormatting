import re

with open('navy_checking.txt', 'r') as f:
    lines = f.readlines()

for line in reversed(lines):
    if "CHASE" in line:
        continue
    if "CITI" in line:
        continue
    if "Credit Card" in line:
        continue

    line = line.strip().replace("\n", "")
    date, location, blank, group, amount, total = line.split("\t")

    location = location.title()
    location = re.sub(r'\S+\s\S+\s-\s', '', location)
    location = re.sub(r'Visa Direct.*', '', location)
    if "AUSGAR" in location:
        location = "Paycheck"

    card = "8887"

    # Format the output string
    output_string = f"{date}@{location}@{card}@{amount}"

    # Print the result
    print(output_string)
