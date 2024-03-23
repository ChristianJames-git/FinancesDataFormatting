from config import ConfigData
from Converters.venmoConverter import venmo_to_sql as venmo
from Converters.citiConverter import costco_to_sql as costco
# from Converters.schwabConverter import schwab_to_sql as schwab_checking
from Converters.chaseConverter import amazon_to_sql as amazon, united_to_sql as united, marriott_to_sql as marriott
# from Converters.navyConverter import navy_to_sql as navy_banking


def run(lines):
    acc = lines[0][0:4]
    if acc == "venm":
        return venmo(lines[1:])
    # elif acc == ConfigData.NAVY_CHECKING:
    #     return navy_banking(lines[1:], acc)
    # elif acc == ConfigData.NAVY_SAVINGS:
    #     return navy_banking(lines[1:], acc)
    # elif acc == ConfigData.NAVY_CREDIT:
    #     return navy_banking(lines[1:], acc)
    # elif acc == ConfigData.NAVY_CD:
    #     return navy_banking(lines[1:], acc)
    elif acc == ConfigData.COSTCO_CARD:
        return costco(lines[1:])
    elif acc == ConfigData.AMAZON_CARD:
        return amazon(lines[1:])
    elif acc == ConfigData.UNITED_CARD:
        return united(lines[1:])
    elif acc == ConfigData.MARRIOTT_CARD:
        return marriott(lines[1:])
    # elif acc == ConfigData.SCHWAB_CHECKING:
    #     return schwab_checking(lines[1:], acc)
    # elif acc == ConfigData.SCHWAB_RENT:
    #     return schwab_checking(lines[1:], acc)


files = [
    # "navy_checking_charges.txt",
    # "navy_savings_charges.txt",
    # "navy_credit_charges.txt",
    # "navy_cd_charges.txt",
    # "schwab_checking_charges.txt",
    # "schwab_rent_charges.txt",
    "costco_charges.txt",
    # "amazon_charges.txt",
    # "united_charges.txt",
    # "marriott_charges.txt",
    # "venmo_charges.txt",
]

with open('charges.txt', 'w') as clear:
    pass
with open('charges.txt', 'a') as output:
    for file in files:
        with open(f"files/{file}", 'r') as f:
            lines = f.readlines()
            for line in run(lines):
                if '\'' in line[1]:
                    line[1] = line[1].replace('\'', '')
                output.write(f"INSERT INTO Transactions (ActualDate, Description, Category, Account, Amount, Tags) VALUES ('{line[0]}', '{line[1]}', '{line[4]}', '{line[2]}', {line[3]}, '');\n")