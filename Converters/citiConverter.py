from datetime import datetime
import re
from config import ConfigData

def costco_to_sheets(lines):
    """
    Input:
        CHICK-FIL-A #02013 619-562-0774 CA
        $12.10
        Feb 21, 2024
        CHRISTIAN JAMES
              
    Output:
        02/21/2024@CHICK-FIL-A@-$12.10
    """
    sheets_lines = []
    lines = [lines[i] for i in range(len(lines)) if "Eligible for Citi" not in lines[i]]
    lines = [lines[i] + lines[i + 1] + lines[i + 2] for i in range(0, len(lines), 5)]

    for line in reversed(lines):
        line = line.strip("\n")
        location, price, date = line.split("\n")
        date = date.strip("\t")
        formatted_date = datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

        location = location.title()
        location = re.sub(r'\s+#*\d.*', '', location)
        location = location.rstrip(" \t")

        price = price.strip().replace(",", "")
        price = float(re.sub(r'[$-]', '', price)) * -1

        # Format the output string
        output_string = f"{formatted_date}@{location}@{ConfigData.COSTCO_CARD}@{price}"

        # Print the result
        # output.write(f"{output_string}\n")
        sheets_lines.append(output_string)
    return sheets_lines
