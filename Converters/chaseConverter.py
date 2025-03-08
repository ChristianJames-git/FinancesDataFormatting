import re
from datetime import datetime

def chase_to_sheets(lines, acc):
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    matches = re.findall(r"((?:\d{2}/\d{2}/\d{4})|(?:[A-Za-z]{3} \d{2}, \d{4}))\n\s*\n*([^\n]+)\n+.*?(-?\$\d+\.\d{2})", text, re.DOTALL)
    formatted_output = [f"{format_date(date)}@{description}@{acc}@{format_amount(amount)}" for date, description, amount in matches]
    formatted_output.sort()

    for output_string in formatted_output:
        sheets_lines.append(output_string)
    return sheets_lines

def format_date(date):
    if "/" in date:
        return date
    return datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

def format_amount(amount):
    if "-" in amount:
        return amount[1:]
    return f"-{amount}"
