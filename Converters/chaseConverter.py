import re
from config import ConfigData

def amazon_to_sheets(output, lines):
    """
    Input:
        Mar 9, 2024	AMZN Mktp US*RN0OC62B2
        Shopping , opens menu	$13.55	
    Output:
        03/09/2024@Amazon@1815@-13.55
    """
    lines = [lines[i] + lines[i + 1] for i in range(0, len(lines), 2)]
    # Process each transaction and print the desired output
    for line in reversed(lines):
        formatted_date, location, price = _chase_to_sheets(line)
        location = "Amazon"
        # Format the output string
        output_string = f"{formatted_date}@{location}@{ConfigData.AMAZON_CARD}@{price}"
        # Print the result
        output.write(f"{output_string}\n")


def united_to_sheets(output, lines):
    """
    Input:
        Feb 22, 2024	CHIPOTLE 1805
        Food & drink , opens menu	$11.04
    Output:
        02/22/2024@Chipotle@0500@-11.04
    """
    lines = [lines[i] + lines[i + 1] for i in range(0, len(lines), 2)]
    # Process each transaction and print the desired output
    for line in reversed(lines):
        formatted_date, location, price = _chase_to_sheets(line)
        # Format the output string
        output_string = f"{formatted_date}@{location}@{ConfigData.UNITED_CARD}@{price}"
        # Print the result
        output.write(f"{output_string}\n")


def marriott_to_sheets(output, lines):
    """
    Input:
        Aug 5, 2023	THE HOME DEPOT 1848
        Home , opens menu	-$64.93		
    Output:
        08/05/2023@The Home Depot@3741@64.93
    """
    lines = [lines[i] + lines[i + 1] for i in range(0, len(lines), 2)]
    # Process each transaction and print the desired output
    for line in reversed(lines):
        formatted_date, location, price = _chase_to_sheets(line)
        # Format the output string
        output_string = f"{formatted_date}@{location}@{ConfigData.MARRIOTT_CARD}@{price}"
        # Print the result
        output.write(f"{output_string}\n")


def _chase_to_sheets(line):
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
    price = float(price.strip().replace(",", "").replace("$", "")) * -1

    return formatted_date, location, price
