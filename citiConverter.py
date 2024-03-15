# input in format below with a space between lines
#   Feb 28, 2023
#   CHIPOTLE 2202 SAN DIEGO US
#   $17.67
# output in format
#   Feb/28/2023 CHIPOTLE -$17.67

# TODO Update to remove "Eligible for Citi Flex Pay" and ending spaces to location

from datetime import datetime
import re

with open('costco.txt', 'r') as f:
    lines = f.readlines()
lines = [lines[i] for i in range(len(lines)) if "Eligible for Citi" not in lines[i]]
lines = [lines[i] + lines[i + 1] + lines[i + 2] for i in range(0, len(lines), 3)]

for line in reversed(lines):
    line = line.strip("\n")
    date, location, price = line.split("\n")
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
