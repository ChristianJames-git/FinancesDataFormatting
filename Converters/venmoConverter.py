from datetime import datetime, timedelta
import re

def venmo_to_sheets(lines):
    sheets_lines = []
    text = "".join(lines)
    combined_lines = re.findall(r"([\s\S]*?\$?\d{1,3}(?:,\d{3})*\.\d{2})\n?", text)

    for line in reversed(combined_lines):
        line = line.split("\n")
        if "Standard Transfer Initiated" not in line[0]:
            desc, date_change, desc2, amount = line
            match = re.search(r"(?:You (?:paid|charged) (.+)|(.+) (?:charged|paid) you)", desc)
            desc = match.group(1) or match.group(2) if match else desc
            desc = f"{desc.strip()} {desc2}"
        else:
            _, date_change, _, _, amount = line
            amount = "-" + amount
            desc = "Venmo Transfer"

        date_change = re.sub(r'\d+[smh]', "0d", date_change)
        if "d" in date_change:
            current_date = datetime.now().date()
            date_change = re.sub(r'\D', '', date_change)
            date = current_date - timedelta(days=int(date_change))
            formatted_date = datetime.strptime(str(date), "%Y-%m-%d").strftime("%m/%d/%Y")
        else:
            if "," not in date_change:
                date_change += ", " + str(datetime.now().year)
            parsed_date = datetime.strptime(date_change, "%b %d, %Y")
            formatted_date = parsed_date.strftime("%m/%d/%Y")

        output_string = f"{formatted_date}@{desc}@{"venmo"}@{re.sub(r"[+ ]", "", amount)}"

        sheets_lines.append(output_string)
    return sheets_lines
