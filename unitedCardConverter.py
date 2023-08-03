import re

with open('united.txt', 'r') as f:
    lines = f.readlines()
lines = [lines[i] + lines[i + 1] for i in range(0, len(lines), 2)]

# Process each transaction and print the desired output
for line in reversed(lines):

    date, location_and_category, price = line.split("\t")

    # Extract location and category from the combined string
    location, category = location_and_category.split("\n")
    location = location.title()  # Capitalize the first letter of each word
    location = re.sub(r'\s*\d.*', '', location)
    location = location.replace("    Pay Over Time", "")

    # Convert the date to the desired format
    from datetime import datetime

    formatted_date = datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

    card = "0500"

    # Remove any leading/trailing whitespaces from price and replace the comma
    price = price.strip().replace(",", "")

    # Hand Card Payments
    if "Payment Thank You" in location:
        location = "Pay United Credit"
        price = price[1:]
        payCardOutput = f"{formatted_date}@{location}@{card}@{price}"
        card = "8887"
        print(payCardOutput)

    # Format the output string
    output_string = f"{formatted_date}@{location}@{card}@-{price}"

    # Print the result
    print(output_string)
