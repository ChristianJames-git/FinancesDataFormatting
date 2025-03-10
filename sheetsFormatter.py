from config import ConfigData
from Converters.venmoConverter import venmo_to_sheets as venmo
from Converters.citiConverter import citi_to_sheets as citi
from Converters.schwabConverter import schwab_to_sheets as schwab_checking
from Converters.navyConverter import navy_to_sheets as navy_banking
from Converters.chaseConverter import chase_to_sheets as chase


def run(lines):
    acc = lines[0][0:4]
    if acc == "venm":
        return venmo(lines[1:])
    elif acc in [ConfigData.NAVY_CHECKING, ConfigData.NAVY_SAVINGS, ConfigData.NAVY_CREDIT, ConfigData.NAVY_CD]:
        return navy_banking(lines[1:], acc)
    elif acc == ConfigData.COSTCO_CARD:
        return citi(lines[1:], acc)
    elif acc in [ConfigData.AMAZON_CARD, ConfigData.UNITED_EXPLORER_CARD, ConfigData.UNITED_QUEST_CARD, ConfigData.MARRIOTT_CARD]:
        return chase(lines[1:], acc)
    elif acc == ConfigData.SCHWAB_CHECKING:
        return schwab_checking(lines[1:], acc)
    elif acc == ConfigData.SCHWAB_RENT:
        return schwab_checking(lines[1:], acc)


files = [
    "navy_checking_charges.txt",
    "navy_savings_charges.txt",
    "navy_cd_charges.txt",
    "schwab_checking_charges.txt",
    "schwab_rent_charges.txt",
    "costco_charges.txt",
    "amazon_charges.txt",
    "united_charges.txt",
    "marriott_charges.txt",
    "venmo_charges.txt",
]

with open('charges.txt', 'w') as clear:
    pass
with open('charges.txt', 'a') as output:
    for file in files:
        with open(f"files/{file}", 'r', encoding="utf-8", errors='ignore') as f:
            lines = f.readlines()
            for line in run(lines):
                output.write(f"{line}\n")