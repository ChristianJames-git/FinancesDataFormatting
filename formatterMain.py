from venmoConverter import venmo_to_sheets as venmo
# from chaseConverter import amazon_to_sheets as amazon, united_to_sheets as united, marriott_to_sheets as marriott
# from citiConverter import costco_to_sheets as costco
# from navyConverter import checking_to_sheets as navy_checking, savings_to_sheets as navy_savings, credit_to_sheets as navy_credit, cd_to_sheets as navy_cd 

with open('charges.txt', 'r') as f:
    lines = f.readlines()
acc = lines[0][0:4]
if acc == "venm":
    venmo(lines[1:])
# elif acc == "8887":
#     navy_checking(lines[1:])
# elif acc == "":
#     navy_savings(lines[1:])
# elif acc == "8818":
#     navy_credit(lines[1:])
# elif acc == "3601":
#     navy_cd(lines[1:])
# elif acc == "0273":
#     costco(lines[1:])
# elif acc == "1815":
#     amazon(lines[1:])
# # elif acc == "0500":
# #     united(lines[1:])
# elif acc == "3741":
#     marriott(lines[1:])