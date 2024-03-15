# TODO Dynamically determine which external accounts money is sent to
from datetime import datetime, timedelta
import re

def venmo_to_sheets(lines):
    """
    Input:
        You paid Eugenio Casta
        1d
        Heater
        - $10.00
    Output:
        03/13/2024@Eugenio Casta Heater@-$10.00
    """
    combined_lines = []
    i = 0
    while i < len(lines):
        combined_string = lines[i] + lines[i + 1] + lines[i + 2] + lines[i + 3]
        i += 4
        combined_lines.append(combined_string)

    for line in reversed(combined_lines):
        line = re.sub(r'\n$', '', line)
        line = line.split("\n")
        if "Standard Transfer Initiated" not in line[0]:
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
            ignore, date_change, ignore2, amount = line
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

        if desc == "Venmo Transfer":
            print(f"{formatted_date}@{desc}@8887@{amount}")
            amount = f"-{amount}"

        card = "venmo"

        output_string = f"{formatted_date}@{desc}@{card}@{amount}"

        # Print the result
        print(output_string)

def venmo_to_sql(lines):
    print("TODO")