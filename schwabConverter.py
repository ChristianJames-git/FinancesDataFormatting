import re
from config import ConfigData
from datetime import datetime

def schwab_to_sheets(lines, acc):
    transactionFound = 0
    transactions_per_date = []
    converts_set = set(_schwab_conversions.keys())

    for line in reversed(lines):
        parts = list(filter(None, line.split("\t")))
        date = parts[0]
        desc = parts[2]
        price = parts[3]
        key = next((key for key in converts_set if key in desc), None)
        if key:
            desc = _schwab_conversions[key](desc)
        _print_transactions(acc, date, desc, price)

def _print_transactions(id, date, desc, price):
    print(f"{date}@{desc}@{id}@{price}")


_schwab_conversions = {
    "Amazon": lambda x: "Amazon Prime",
}