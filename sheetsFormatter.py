# TODO schwab
# TODO navyfed
from config import ConfigData
from venmoConverter import venmo_to_sheets as venmo
from citiConverter import costco_to_sheets as costco
# from schwabConverter import checking_to_sheets as schwab_checking, rent_to_sheets as rent 
from chaseConverter import amazon_to_sheets as amazon, united_to_sheets as united, marriott_to_sheets as marriott
from navyConverter import checking_to_sheets as navy_checking, savings_to_sheets as navy_savings, credit_to_sheets as navy_credit, cd_to_sheets as navy_cd 

with open('navy_checking_charges.txt', 'r') as f:
    lines = f.readlines()
acc = lines[0][0:4]
if acc == "venm":
    venmo(lines[1:])
elif acc == ConfigData.NAVY_CHECKING:
    navy_checking(lines[1:])
elif acc == ConfigData.NAVY_SAVINGS:
    navy_savings(lines[1:])
elif acc == ConfigData.NAVY_CREDIT:
    navy_credit(lines[1:])
elif acc == ConfigData.NAVY_CD:
    navy_cd(lines[1:])
elif acc == ConfigData.COSTCO_CARD:
    costco(lines[1:])
elif acc == ConfigData.AMAZON_CARD:
    amazon(lines[1:])
elif acc == ConfigData.UNITED_CARD:
    united(lines[1:])
elif acc == ConfigData.MARRIOTT_CARD:
    marriott(lines[1:])
# elif acc == ConfigData.SCHWAB_CHECKING:
#     schwab_checking(lines[1:])
# elif acc == ConfigData.SCHWAB_RENT:
#     rent(lines[1:])