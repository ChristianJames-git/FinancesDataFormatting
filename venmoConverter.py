# Input:
#   You paid Eugenio Casta
#   1d
#   Heater
#   - $10.00
# Output:
#   2023-02-28 Eugenio Casta Heater -$10.00

from datetime import datetime, timedelta
import re

with open('venmos.txt', 'r') as f:
    lines = f.readlines()
combined_lines = []
i = 0
while i < len(lines):
    if "Standard Transfer Initiated" in lines[i]:
        combined_string = lines[i] + lines[i + 1] + lines[i + 2] + lines[i + 3] + lines[i + 4]
        i += 5
    else:
        combined_string = lines[i] + lines[i + 1] + lines[i + 2] + lines[i + 3]
        i += 4
    combined_lines.append(combined_string)

for line in reversed(combined_lines):
    line = re.sub(r'\n$', '', line)
    line = line.split("\n")
    if len(line) == 4:
        desc, date_change, desc2, amount = line
        you_paid_pattern = re.compile(r'You paid (.+)')
        paid_you_pattern = re.compile(r'(.+) paid you')
        you_charged_pattern = re.compile(r'You charged (.+)')
        charged_you_pattern = re.compile(r'(.+) charged you')

        # Try to find matches for both patterns
        you_paid_match = you_paid_pattern.search(desc)
        paid_you_match = paid_you_pattern.search(desc)
        you_charged_match = you_charged_pattern.search(desc)
        charged_you_match = charged_you_pattern.search(desc)

        if you_paid_match:
            description = you_paid_match.group(1)
            desc = you_paid_pattern.sub(description, desc)
        elif paid_you_match:
            description = paid_you_match.group(1)
            desc = paid_you_pattern.sub(description, desc)
        elif you_charged_match:
            description = you_charged_match.group(1)
            desc = you_charged_pattern.sub(description, desc)
        elif charged_you_match:
            description = charged_you_match.group(1)
            desc = charged_you_pattern.sub(description, desc)
        desc = f"{desc.strip()} {desc2}"
    else:
        ignore, date_change, ignore2, ignore3, amount = line
        desc = "Venmo Transfer"

    date_change = re.sub(r'\d+[smh]', "0d", date_change)
    if "d" in date_change:
        current_date = datetime.now().date()
        date_change = re.sub(r'\D', '', date_change)
        date = current_date - timedelta(days=int(date_change))
        formatted_date = datetime.strptime(str(date), "%Y-%m-%d").strftime("%m/%d/%Y")
    else:
        current_year = datetime.now().year
        parsed_date = datetime.strptime(date_change, "%b %d")
        formatted_date = parsed_date.replace(year=current_year).strftime("%m/%d/%Y")

    amount = re.sub(' ', '', amount)
    amount = re.sub('\+', '', amount)

    if len(line) == 5:
        amount = f"-{amount}"

    card = "venmo"

    output_string = f"{formatted_date}@{desc}@{card}@{amount}"

    # Print the result
    print(output_string)
