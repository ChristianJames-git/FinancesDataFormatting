from config import ConfigData
from venmoConverter import venmo_to_sheets as venmo
from citiConverter import costco_to_sheets as costco
from schwabConverter import schwab_to_sheets as schwab_checking
from chaseConverter import amazon_to_sheets as amazon, united_to_sheets as united, marriott_to_sheets as marriott
from navyConverter import navy_to_sheets as navy_banking

with open('schwab_rent_charges.txt', 'r') as f:
    lines = f.readlines()
acc = lines[0][0:4]
if acc == "venm":
    venmo(lines[1:])
elif acc == ConfigData.NAVY_CHECKING:
    navy_banking(lines[1:], acc)
elif acc == ConfigData.NAVY_SAVINGS:
    navy_banking(lines[1:], acc)
elif acc == ConfigData.NAVY_CREDIT:
    navy_banking(lines[1:], acc)
elif acc == ConfigData.NAVY_CD:
    navy_banking(lines[1:], acc)
elif acc == ConfigData.COSTCO_CARD:
    costco(lines[1:])
elif acc == ConfigData.AMAZON_CARD:
    amazon(lines[1:])
elif acc == ConfigData.UNITED_CARD:
    united(lines[1:])
elif acc == ConfigData.MARRIOTT_CARD:
    marriott(lines[1:])
elif acc == ConfigData.SCHWAB_CHECKING:
    schwab_checking(lines[1:], acc)
elif acc == ConfigData.SCHWAB_RENT:
    schwab_checking(lines[1:], acc)