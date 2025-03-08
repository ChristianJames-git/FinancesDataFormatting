from datetime import datetime
import re

def citi_to_sheets(lines, acc):
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    
    matches = re.findall(r"([A-Za-z0-9]+(?: [^\n\d\#]+)*)[\s\S]*?(-?\$?\d{1,3}(?:,\d{3})*\.\d{2})\s*?([A-Za-z]{3} \d{2}, \d{4})\s*?CHRISTIAN JAMES", text)

    formatted_output = [f"{format_date(date)}@{description.strip()}@{acc}@{format_amount(amount)}" for description, amount, date in matches]
    formatted_output.sort()

    for output_string in formatted_output:
        sheets_lines.append(output_string)

    return sheets_lines

def format_date(date):
    return datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

def format_amount(amount):
    if "-" in amount:
        return amount[1:]
    return f"-{amount}"