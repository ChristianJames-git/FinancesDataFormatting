from datetime import datetime
import re

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

        card = "0287"

        price = price.strip().replace(",", "")

        if "Autopay" in location:
            location = f"Pay Costco Credit"
            price = price[1:]
            payCardOutput = f"{formatted_date}@{location}@{card}@{price}"
            card = "8887"
            print(payCardOutput)

        # Format the output string
        output_string = f"{formatted_date}@{location}@{card}@-{price}"

        # Print the result
        print(output_string)
