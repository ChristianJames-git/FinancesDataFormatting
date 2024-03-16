import re
from config import ConfigData
from datetime import datetime

def checking_to_sheets(lines):
    transactionFound = 0
    transactions_per_date = []

    for line in reversed(lines):
        if not transactionFound:
            if "Transaction Amount" in line:
                transactionFound = 3
            elif bool(re.search(r',\s20\d{2}\n', line)):
                _print_transactions(ConfigData.NAVY_CHECKING, transactions_per_date, line.strip())
                transactions_per_date.clear()
                continue
            else:
                continue
        if transactionFound == 3:
            match = re.search(r'Transaction Amount(-?\$\d+(?:,\d{3})*\.\d{2})', line)
            transactions_per_date.append(match.group(1))
        elif transactionFound == 1:
            transactions_per_date.append(line.strip())
        transactionFound -= 1
        continue
        # if "CHASE" in line:
        #     continue
        # if "CITI" in line:
        #     continue
        # if "Credit Card" in line:
        #     continue
        # if "VENMO CASHOUT" in line:
        #     continue

        # line = line.strip().replace("\n", "")
        # date, location, blank, group, amount, total = line.split("\t")

        # location = location.title()
        # location = re.sub(r'\S+\s\S+\s-\s', '', location)
        # location = re.sub(r'Visa Direct.*', '', location)
        # if "AUSGAR" in location:
        #     location = "Paycheck"

        # card = ConfigData.NAVY_CHECKING

        # # Format the output string
        # output_string = f"{date}@{location}@{card}@{amount}"

        # # Print the result
        # print(output_string)


def savings_to_sheets(lines):
    print(lines)


def cd_to_sheets(lines):
    print(lines)


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
            print(f"{date}@{location}@{ConfigData.MAIN_ACCOUNT}@-{amount}")
        elif "Amazon Prime" in location:
            location = "Amazon Prime"
        else:
            location = location.split(" ")[0]
            location = location.title()

        # Format the output string
        output_string = f"{date}@{location}@{card}@{amount}"

        # Print the result
        print(output_string)


def _is_valid_date(date):
    # Define the expected date format
    date_format = "%B %d, %Y"
    # Attempt to parse the date string
    parsed_date = datetime.strptime(date, date_format)
    # Check if the parsed date matches the original string
    return parsed_date.strftime(date_format) == date


def _print_transactions(id, transaction_list, date):
    print(transaction_list)
    print(date)