from config import ConfigData
from venmoConverter import venmo_to_sheets as venmo
from citiConverter import costco_to_sheets as costco
from schwabConverter import schwab_to_sheets as schwab_checking
from chaseConverter import amazon_to_sheets as amazon, united_to_sheets as united, marriott_to_sheets as marriott
from navyConverter import navy_to_sheets as navy_banking


def run(lines):
    acc = lines[0][0:4]
    if acc == "venm":
        venmo(output, lines[1:])
    elif acc == ConfigData.NAVY_CHECKING:
        navy_banking(output, lines[1:], acc)
    elif acc == ConfigData.NAVY_SAVINGS:
        navy_banking(output, lines[1:], acc)
    elif acc == ConfigData.NAVY_CREDIT:
        navy_banking(output, lines[1:], acc)
    elif acc == ConfigData.NAVY_CD:
        navy_banking(output, lines[1:], acc)
    elif acc == ConfigData.COSTCO_CARD:
        costco(output, lines[1:])
    elif acc == ConfigData.AMAZON_CARD:
        amazon(output, lines[1:])
    elif acc == ConfigData.UNITED_CARD:
        united(output, lines[1:])
    elif acc == ConfigData.MARRIOTT_CARD:
        marriott(output, lines[1:])
    elif acc == ConfigData.SCHWAB_CHECKING:
        schwab_checking(output, lines[1:], acc)
    elif acc == ConfigData.SCHWAB_RENT:
        schwab_checking(output, lines[1:], acc)


files = [
    "navy_checking_charges.txt",
    "navy_savings_charges.txt",
    "navy_credit_charges.txt",
    "navy_cd_charges.txt",
    "schwab_checking_charges.txt",
    "schwab_rent_charges.txt",
    "costco_charges.txt",
    "amazon_charges.txt",
    # "united_charges.txt",
    # "marriott_charges.txt",
    "venmo_charges.txt",
]

with open('charges.txt', 'w') as clear:
    pass
with open('charges.txt', 'a') as output:
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            run(lines)