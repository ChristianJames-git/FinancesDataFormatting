import re
from datetime import datetime

def navy_to_sheets(lines, acc):
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")

    date_blocks = re.findall(r"(\b[A-Za-z]+ \d{1,2}, \d{4}\b)([\s\S]*?)(?=\b[A-Za-z]+ \d{1,2}, \d{4}\b|$)", text)
    formatted_output = []
    
    for date_str, transactions in date_blocks:
        date = format_date(date_str.strip())
        
        matches = re.findall(r"([^\n]+)\n.*?Transaction Amount\s*(-?\$?\d{1,3}(?:,\d{3})*\.\d{2})", transactions, re.DOTALL)
        
        for description, amount in matches:
            formatted_output.append(f"{date}@{description.strip()}@{acc}@{amount}")
    
    formatted_output.sort()
    sheets_lines.extend(formatted_output)
    return sheets_lines

def format_date(date_str):
    return datetime.strptime(date_str, "%B %d, %Y").strftime("%m/%d/%Y")
