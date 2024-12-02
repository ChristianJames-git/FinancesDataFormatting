import re
import sys
sys.path.append(r'C:\\Users\\Christian\\Documents\\Coding\SQL\\PersonalFinances\\FinancesDataFormatting')
from datetime import datetime
import PyPDF2
from config import ConfigData

def navy_to_sheets(lines, acc):
    sheets_lines = []
    transactionFound = 0
    transactions_per_date = []
    converts_set = set(_navy_conversions.keys())

    for line in reversed(lines):
        if not transactionFound:
            if "Transaction Amount" in line:
                transactionFound = 3
            elif bool(re.search(r',\s20\d{2}\n', line)):
                _print_transactions(sheets_lines, acc, transactions_per_date, line.strip())
                transactions_per_date.clear()
                continue
            else:
                continue
        if transactionFound == 3:
            match = re.search(r'Transaction Amount(-?\$\d+(?:,\d{3})*\.\d{2})', line)
            transactions_per_date.append(match.group(1))
        elif transactionFound == 1:
            desc = line.strip()
            key = next((key for key in converts_set if key in desc), None)
            if key:
                desc = _navy_conversions[key](desc)
        
            transactions_per_date.append(desc)
        transactionFound -= 1
        continue
    return sheets_lines


def navy_to_sql(lines, acc):
    sheets_lines = navy_to_sheets(lines, acc)
    sql_lines = []
    for line in sheets_lines:
        date, desc, account, price = line.split('@')
        category = 'Shopping'
        if "Payment" in desc:
            category = 'Transfer'
        if "Income" in desc:
            category = "Income"
        for restaurant in _category_helper["Restaurants"]:
            if restaurant in desc:
                category = 'Restaurant'
                break
        sql_lines.append([date, desc, account, price, category])
    return sql_lines


files = [
]


def navy_checking_savings_statement():
    with open('charges.txt', 'w') as clear:
        pass
    with open('charges.txt', 'a') as output:
        data = []
        for file in files:
            with open(f"files/{file}", 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                num_pages = len(reader.pages)
                text = ''
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                lines = text.split('\n')
                stage = 0
                descs = []
                totals = []
                year = file[0:4]
                for line in lines:
                    if "Christian" in line or "CHRISTIAN" in line:
                        continue
                    if stage == 1:
                        stage = 2
                        continue
                    elif "Joint Owner(s)" in line:
                        stage = 1
                    elif stage == 2:
                        totals.append(line)
                        if "Statement Period" in line:
                            stage = 3
                    elif stage in [ConfigData.NAVY_CHECKING, ConfigData.NAVY_SAVINGS, ConfigData.NAVY_MM]:
                        if "Date Transaction Detail" in line or "SAVINGS DIVIDENDS" in line:
                            stage = 0
                        elif "Beginning Balance" in line:
                            stage = ConfigData.NAVY_MM
                        else:
                            descs.append((line, stage))
                    elif "Beginning Balance" in line:
                        if descs:
                            stage = ConfigData.NAVY_SAVINGS
                        else:
                            stage = ConfigData.NAVY_CHECKING
                for desc, total in zip(descs, totals):
                    date, description = desc[0].split(' ', 1)
                    date = date.replace('-', '/') + '/' + str(year)
                    price = re.search(r'\d{1,3}(?:,\d{3})*\.\d{2}', total).group()
                    data.append((date, description.strip(), price, desc[1]))
        for date, desc, amount, account in data:
            category = "Income"
            tags = ''
            amount = amount.replace(',', '')
            if "Acorns" in desc:
                if "Subscription" in desc:
                    desc, category, tags = "Acorns", "Shopping", "Subscription"
                else:
                    desc, category = "Acorns Transfer", "Transfer"
            elif "Venmo" in desc:
                desc, category = "Venmo Transfer", "Transfer"
            elif "Zelle*reina" in desc:
                desc, category, tags = "Reina Rent", "Bills", "Rent ; Reina"
            elif "Zelle*zack" in desc:
                desc, category, tags = "Zack Rent", "Bills", "Rent ; Zack"
            elif "Zelle*eugenio" in desc:
                desc, category, tags = "Eugenio Rent", "Bills", "Rent ; Eugenio"
            elif "Zelle*minseo" in desc:
                desc, category, tags = "Kluke Rent", "Bills", "Rent ; Kluke"
            elif "Paypal" in desc and float(amount) > 750:
                desc, category, tags = "Luke Rent", "Bills", "Rent ; Luke"
            elif "Reward Redemption" in desc:
                category, tags = "Shopping", "Rewards"
            elif "Schwab" in desc:
                desc, category, tags = "Transfer to Schwab", "Transfer", "Brokerage ; "
            elif "Check" in desc and float(amount) > 3500:
                category, tags = "Bills", "Rent"
            elif "Transfer To Credit Card" in desc:
                category = "Transfer"
            elif "D James" in desc:
                desc, tags = "Opa 529", "529"
            elif "Sandiego Water" in desc:
                desc, category = "City of San Diego Water", "Bills"
            elif "Citi" in desc:
                desc, category = "Pay Citi Credit", "Transfer"
            elif "Chase" in desc:
                desc, category = "Pay Chase Credit", "Transfer"
            elif "Payroll" in desc:
                desc, tags = "Paycheck", "Work"
            elif "Scan/Mobile" in desc and amount == "830.00":
                desc, category, tags = "Chwis Rent", "Bills", "Rent ; Chwis"
            output.write(f"INSERT INTO Transactions (ActualDate, Description, Category, Account, Amount, Tags) VALUES ('{date}', '{desc}', '{category}', '{account}', {amount}, '{tags}');\n")


def navy_credit_annual_statement():
    with open('charges.txt', 'w') as clear:
        pass
    with open('charges.txt', 'a') as output:
        with open(f"files/navy_credit_charges.txt", 'r') as f:
            lines = f.readlines()
            pattern = re.compile(r'(\d{2}/\d{2}/\d{2})\s+(.*?)\s+(\d+\.\d{2})')
            for line in lines:
                if line == "8818\n":
                    continue
                line = line.replace(',', '')
                line = line.replace('\'', '')
                match = pattern.match(line.strip())
                date, desc, amount = match.group(1), match.group(2), match.group(3)
                if 'CHIPOTLE' in desc:
                    desc = "Chipotle"
                if 'JACK' in desc:
                    desc = "Jack in the Box"
                if 'POKI' in desc:
                    desc = "Poki"
                if 'SHAKE SMART' in desc:
                    desc = "Shake Smart"
                if 'PANDA EXPRESS' in desc:
                    desc = "Panda"
                if 'EPIC WINGS' in desc:
                    desc = "Wings"
                if 'SOMBRERO' in desc:
                    desc = "Sombreros"
                if 'ADALBERTOS' in desc:
                    desc = "Adalbertos"
                if 'PHO CA DAO' in desc:
                    desc = "Pho Ca Dao"
                if 'DOMINO' in desc:
                    desc = "Dominos"
                if 'LUCKY' in desc:
                    desc = "Lucky Chinese"
                if 'UNDERBELLY' in desc:
                    desc = "Underbelly"
                if 'VINNIES' in desc:
                    desc = "Vinnies"
                if 'IN N OUT' in desc:
                    desc = "InNOut"
                output.write(f"INSERT INTO Transactions (ActualDate, Description, Category, Account, Amount, Tags) VALUES ('{date}', '{desc}', 'Shopping', '{ConfigData.NAVY_CREDIT}', -{amount}, '');\n")
        


def _print_transactions(sheets_lines: list, id, transaction_list, date):
    formatted_date = datetime.strptime(date, "%B %d, %Y").strftime("%m/%d/%Y")
    for i in range(0, len(transaction_list), 2):
        description = transaction_list[i+1]
        price = transaction_list[i]
        output_string = f"{formatted_date}@{description}@{id}@{price}"
        # output.write(f"{formatted_date}@{description}@{id}@{price}\n")
        sheets_lines.append(output_string)


_navy_conversions = {
    "Amazon": lambda x: "Amazon Prime",
    "8818": lambda x: x[:-7],
    "Ausgar": lambda x: "Paycheck",
    "Dividend": lambda x: "Interest Income",
    "DIVIDEND": lambda x: "Interest Income",
    "Interest": lambda x: "Interest Income",
    "Investment Income": lambda x: "Interest Income",
    "TRF FR CERT-SHR": lambda x: "Transfer",
    "Transfer To Credit Car": lambda x: "Transfer To Credit Card"
}


_category_helper = {
    "Restaurants": ['Sakana', 'Panda Express', 'Domino', 'Pho', 'Tajima', 'Chick-Fil-A', 'Popeyes', 'Carls', 'Adalbertos', 'Church\'S Chicken', 'Starbucks', 'Sushi', 'Dragonburger', 'Mcdonald', 'Cafe', 'Wendys', 'Poki', 'Chinese', 'Jack', 'Chipotle']
}
