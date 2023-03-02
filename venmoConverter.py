# Input:
#   You paid Eugenio Casta
#   1d
#   Heater
#   - $10.00
# Output:
#   2023-02-28 Eugenio Casta Heater -$10.00

from datetime import date as datet
from datetime import timedelta

with open('venmos.txt', 'r') as f:
    lines = f.readlines()

count = 1
transfer = ""
today = datet.today()
date = datet.today()
desc = ""
amount = ""
payments = []
for line in lines:
    line = line.strip("\n")
    match count:
        case 1:
            splitLine = line.split(" ")
            if line[0] == 'Y':  # case for me paying or chargine
                desc = f"{splitLine[2]} {splitLine[3]}"
            elif line[0:12] == "Bank Transfer": #  case for bank transfer
                desc = f"Transfer Venmo"
            else:  # case for me being paid or charged
                desc = f"{splitLine[0]} {splitLine[1]}"
        case 2:
            if line[len(line)-1] == 'h':
                date = today
            elif line[len(line)-1] == 'd':
                date = today - timedelta(days=int(line[0:len(line)-1]))  # subtract days
        case 3:
            if line[0:18] == "Estimated arrival:":
                transfer = "-"
                continue
            desc = f"{desc} {line}"
        case 4:
            line = line.replace(" ", "")
            amount = f"{transfer}{line}"
            transfer = ""
            payments.append(f"{date} {desc} {amount}")
            count = 0
    count += 1

payments.reverse()
for payment in payments:                                                    
    print(payment)
