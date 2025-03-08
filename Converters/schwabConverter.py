import re

def schwab_to_sheets(lines, acc):
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    
    matches = re.findall(r"(\d{2}/\d{2}/\d{4})\t[A-Z]+\t+([^	]+?)\t(\t?)(\$?\d{1,3}(?:,\d{3})*\.\d{2})[\s\S]*?\n?", text)

    formatted_output = [f"{date}@{description.strip()}@{acc}@{format_amount(amount, tab)}" for date, description, tab, amount in matches]
    formatted_output.sort()

    for output_string in formatted_output:
        sheets_lines.append(output_string)

    return sheets_lines

def format_amount(amount, tab):
    if not tab:
        amount = "-" + amount
    return amount