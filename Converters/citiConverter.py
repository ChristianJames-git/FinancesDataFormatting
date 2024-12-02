from datetime import datetime
import re
from config import ConfigData

# TODO Remove San Diego CA from charges

def costco_to_sheets(lines):
    """
    Input:	
        8218 GREAT CLIPS AT SANTESANTEE CA	
        $30.00
        Mar 30, 2024
        CHRISTIAN JAMES
              
    Output:
        03/30/2024@8218 GREAT CLIPS@-$30.00
    """

    sheets_lines = []
    lines = [lines[i] for i in range(len(lines)) if ("Eligible for Citi" not in lines[i] and "                " not in lines[i])]
    lines = [lines[i] + lines[i + 1] + lines[i + 2] for i in range(0, len(lines), 3)]

    for line in reversed(lines):
        line = line.strip("\n")
        date, location, price = line.split("\n")
        date = date.strip("\t")
        formatted_date = datetime.strptime(date, "%b %d, %Y").strftime("%m/%d/%Y")

        location = location.title()
        location = re.sub(r'\s+#*\d.*', '', location)
        location = location.rstrip(" \t").replace('@', '')

        price = price.strip().replace(",", "")
        price = float(re.sub(r'[$]', '', price)) * -1

        # Format the output string
        output_string = f"{formatted_date}@{location}@{ConfigData.COSTCO_CARD}@{price}"

        # Print the result
        # output.write(f"{output_string}\n")
        sheets_lines.append(output_string)
    return sheets_lines

def costco_to_sql(lines):
    sheets_lines = costco_to_sheets(lines)
    sql_lines = []
    for line in sheets_lines:
        date, desc, account, price = line.split('@')
        category = 'Shopping'
        if "Autopay" in desc:
            category = 'Transfer'
            desc = "Costco Payment"
        for restaurant in _category_helper["Restaurants"]:
            if restaurant in desc:
                category = 'Restaurant'
                break
        sql_lines.append([date, desc, account, price, category])
    return sql_lines


_category_helper = {
    "Restaurants": ['Sakana', 'Panda Express', 'Domino', 'Pho', 'Tajima', 'Chick-Fil-A', 'Popeyes', 'Carls', 'Adalbertos', 'Church\'S Chicken', 'Starbucks', 'Sushi', 'Dragonburger', 'Mcdonald', 'Cafe', 'Wendys', 'Poki', 'Chinese', 'Jack', 'Chipotle']
}