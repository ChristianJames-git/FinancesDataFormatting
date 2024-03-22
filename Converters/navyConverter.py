import re
from datetime import datetime

def navy_to_sheets(lines, acc):
    sheets_lines = []
    transactionFound = 0
    transactions_per_date = []
    converts_set = set(_navy_conversions.keys())

    for line in reversed(lines):
        if not transactionFound:
            if "Transaction Amount" in line:
                transactionFound = 3
            elif bool(re.search(r',\s20\d{2}\n', line)):
                _print_transactions(sheets_lines, acc, transactions_per_date, line.strip())
                transactions_per_date.clear()
                continue
            else:
                continue
        if transactionFound == 3:
            match = re.search(r'Transaction Amount(-?\$\d+(?:,\d{3})*\.\d{2})', line)
            transactions_per_date.append(match.group(1))
        elif transactionFound == 1:
            desc = line.strip()
            key = next((key for key in converts_set if key in desc), None)
            if key:
                desc = _navy_conversions[key](desc)
        
            transactions_per_date.append(desc)
        transactionFound -= 1
        continue
    return sheets_lines


def _print_transactions(sheets_lines: list, id, transaction_list, date):
    formatted_date = datetime.strptime(date, "%B %d, %Y").strftime("%m/%d/%Y")
    for i in range(0, len(transaction_list), 2):
        description = transaction_list[i+1]
        price = transaction_list[i]
        output_string = f"{formatted_date}@{description}@{id}@{price}"
        # output.write(f"{formatted_date}@{description}@{id}@{price}\n")
        sheets_lines.append(output_string)


_navy_conversions = {
    "Amazon": lambda x: "Amazon Prime",
    "8818": lambda x: x[:-7],
    "Ausgar": lambda x: "Work Ausgar",
    "Dividend": lambda x: "Interest Income",
    "DIVIDEND": lambda x: "Interest Income",
    "Interest": lambda x: "Interest Income",
    "Investment Income": lambda x: "Interest Income",
    "TRF FR CERT-SHR": lambda x: "Transfer"
}