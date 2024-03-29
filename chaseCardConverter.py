import re

with open('chase.txt', 'r') as f:
    lines = f.readlines()
card = lines[0][0:4]
lines = [lines[i] + lines[i + 1] for i in range(1, len(lines), 2)]

# Process each transaction and print the desired output
for line in reversed(lines):

    finalcard = card
    line = line.strip("\n")
    line = line.strip("\t")
    date, location_and_category, price = line.split("\t")

    # Extract location and category from the combined string
    location, category = location_and_category.split("\n")
    location = location.title()  # Capitalize the first letter of each word
    location = re.sub(r'\s+\d.*', '', location)
    location = location.replace("    Pay Over Time", "")

    # Convert the date to the desired format
    from datetime import datetime
    formatted_date = datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

    # Remove any leading/trailing whitespaces from price and replace the comma
    price = price.strip().replace(",", "")

    if "-" in price and card == "3741":
        print(f"{formatted_date}@{location}@{finalcard}@{price[1:]}")
        continue

    # Hand Card Payments
    if "Payment" in location:
        match card:
            case "0500":
                cardName = "United"
            case "1815":
                cardName = "Amazon"
            case "3741":
                cardName = "Marriott"
            case _:
                cardName = "ERROR"

        location = f"Pay {cardName} Credit"
        price = price[1:]
        payCardOutput = f"{formatted_date}@{location}@{finalcard}@{price}"
        finalcard = "8887"
        print(payCardOutput)
    else:
        if card == "1815":
            location = "Amazon"
        if "-" in price:
            print(f"{formatted_date}@{location}@{finalcard}@{price.strip('-')}")
            continue

    # Format the output string
    output_string = f"{formatted_date}@{location}@{finalcard}@-{price}"

    # Print the result
    print(output_string)
