# input in format below with a space between lines
#   Feb 28, 2023
#   CHIPOTLE 2202 SAN DIEGO US
#   $17.67
# output in format
#   Feb/28/2023 CHIPOTLE -$17.67

with open('costco.txt', 'r') as f:
    lines = f.readlines()

count = 1
month = ""
day = ""
year = ""
desc = ""
amount = ""
payments = []
for line in lines:
    if line.strip() == "":
        count = 1
        continue
    if count == 1:
        month, day, year = line.split(" ")
        day = day.replace(',', "")
        year = year.strip()
        count = 2
        continue
    if count == 2:
        desc = line.split(" ")
        count = 3
        continue
    if count == 3:
        amount = "-" + line.strip()[1:]
        payments.append(f"{month}/{day}/{year} {desc[0]} {amount}")
        continue
payments.reverse()
for payment in payments:
    print(payment)

