import re

def checking_to_sheets(lines):
    for line in reversed(lines):
        if "CHASE" in line:
            continue
        if "CITI" in line:
            continue
        if "Credit Card" in line:
            continue
        if "VENMO CASHOUT" in line:
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


def credit_to_sheets(lines):
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
            location = location.title()

        # Format the output string
        output_string = f"{date}@{location}@{card}@{amount}"

        # Print the result
        print(output_string)
