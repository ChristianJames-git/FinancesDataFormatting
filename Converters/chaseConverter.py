import re
from config import ConfigData
from datetime import datetime

def amazon_to_sheets(lines):
    """
    Input:
        Mar 9, 2024	AMZN Mktp US*RN0OC62B2
        Shopping , opens menu	$13.55	
    Output:
        03/09/2024@Amazon@1815@-13.55
    """
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    matches = re.findall(r"((?:\d{2}/\d{2}/\d{4})|(?:[A-Za-z]{3} \d{2}, \d{4}))\n(.*?)\n.*?(\-?\$\d+\.\d{2})", text, re.DOTALL)
    formatted_output = [f"{format_date(date)}@Amazon@{ConfigData.AMAZON_CARD}@{format_amount(amount)}" for date, description, amount in matches]
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


def united_to_sheets(lines):
    """
    Input:
        Feb 22, 2024	CHIPOTLE 1805
        Food & drink , opens menu	$11.04
    Output:
        02/22/2024@Chipotle@0500@-11.04
    """
    sheets_lines = []
    text = "\n".join(lines)
    text = text.replace("−", "-")
    matches = re.findall(r"((?:\d{2}/\d{2}/\d{4})|(?:[A-Za-z]{3} \d{2}, \d{4}))\n\s*\n*([^\n]+)\n+.*?(-?\$\d+\.\d{2})", text, re.DOTALL)
    formatted_output = [f"{format_date(date)}@{description}@{ConfigData.UNITED_EXPLORER_CARD}@{format_amount(amount)}" for date, description, amount in matches]
    formatted_output.sort()

    for output_string in formatted_output:
        sheets_lines.append(output_string)
    return sheets_lines


def marriott_to_sheets(lines):
    """
    Input:
        Aug 5, 2023	THE HOME DEPOT 1848
        Home , opens menu	-$64.93		
    Output:
        08/05/2023@The Home Depot@3741@64.93
    """
    sheets_lines = []
    text = "".join(lines)
    text = text.replace("−", "-")
    matches = re.findall(r"((?:\d{2}/\d{2}/\d{4})|(?:[A-Za-z]{3} \d{2}, \d{4}))\n([^\n]+)\n(?:[^\n]*\n)*?(\-?\$\d+\.\d{2})", text)
    formatted_output = [f"{format_date(date)}@{description}@{ConfigData.MARRIOTT_CARD}@{format_amount(amount)}" for date, description, amount in matches]

    for output_string in formatted_output:
        sheets_lines.append(output_string)
    return sheets_lines


# def amazon_to_sql(lines):
#     sheets_lines = amazon_to_sheets(lines)
#     sql_lines = []
#     for line in sheets_lines:
#         date, desc, account, price = line.split('@')
#         category = 'Shopping'
#         if "Payment" in desc:
#             category = 'Transfer'
#         sql_lines.append([date, desc, account, price, category])
#     return sql_lines


# def united_to_sql(lines):
#     sheets_lines = united_to_sheets(lines)
#     sql_lines = []
#     for line in sheets_lines:
#         date, desc, account, price = line.split('@')
#         category = 'Shopping'
#         if "Payment" in desc:
#             category = 'Transfer'
#         for restaurant in _category_helper["Restaurants"]:
#             if restaurant in desc:
#                 category = 'Restaurant'
#                 break
#         sql_lines.append([date, desc, account, price, category])
#     return sql_lines


# def marriott_to_sql(lines):
#     sheets_lines = marriott_to_sheets(lines)
#     sql_lines = []
#     for line in sheets_lines:
#         date, desc, account, price = line.split('@')
#         category = 'Shopping'
#         if "Payment" in desc:
#             category = 'Transfer'
#         for restaurant in _category_helper["Restaurants"]:
#             if restaurant in desc:
#                 category = 'Restaurant'
#                 break
#         sql_lines.append([date, desc, account, price, category])
#     return sql_lines


# _category_helper = {
#     "Restaurants": ['Sakana', 'Panda Express', 'Domino', 'Pho', 'Tajima', 'Chick-Fil-A', 'Popeyes', 'Carls', 'Adalbertos', 'Church\'S Chicken', 'Starbucks', 'Sushi', 'Dragonburger', 'Mcdonald', 'Cafe', 'Wendys', 'Poki', 'Chinese', 'Jack', 'Chipotle']
# }