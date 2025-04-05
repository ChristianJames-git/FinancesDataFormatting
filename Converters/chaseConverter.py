import re
from datetime import datetime

def chase_to_sheets(lines, acc):
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    
    '''
        ((?:\\d{2}/\\d{2}/\\d{4})|(?:[A-Za-z]{3} \\d{2}, \\d{4}))
            Matches DATE. Either 01/01/2025 format or Jan 01, 2025 format. "?:" means non-capturing.
        \n\s*\n*
            Newline, optional whitespaces, optional newlines
        ([^\n]+)
            Matches one line (no newlines) - DESCRIPTION
        \n+.*?
            Newline (1 or more). Then Lazy match anything until the next regex block.
        (-?\$\\d{1,3}(?:,\\d{3})*\.\\d{2})
            AMOUNT. Optional "-" ; "$" ; first amount block before "," or "." ; any comma-separated triplets ",###" ; decimal cents ".##"
    '''
    matches = re.findall(r"((?:\d{2}/\d{2}/\d{4})|(?:[A-Za-z]{3} \d{2}, \d{4}))\n\s*\n*([^\n]+)\n+.*?(-?\$\d{1,3}(?:,\d{3})*\.\d{2})", text, re.DOTALL)
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
