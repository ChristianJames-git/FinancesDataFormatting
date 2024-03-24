def schwab_to_sheets(lines, acc):
    sheets_lines = []
    converts_set = set(_schwab_conversions.keys())

    for line in reversed(lines):
        # parts = list(filter(None, line.split("\t")))
        parts = list(line.strip().split("\t"))
        date = parts[0]
        desc = parts[3]
        if parts[4]:
            price = "-" + parts[4]
        else:
            price = parts[5]
        key = next((key for key in converts_set if key in desc), None)
        if key:
            desc = _schwab_conversions[key](desc)
        output_string = f"{date}@{desc}@{acc}@{price}"
        # output.write(f"{date}@{desc}@{acc}@{price}\n")
        sheets_lines.append(output_string)
    return sheets_lines


def schwab_to_sql(lines, acc):
    sheets_lines = schwab_to_sheets(lines, acc)
    sql_lines = []
    for line in sheets_lines:
        date, desc, account, price = line.split('@')
        category = 'Shopping'
        sql_lines.append([date, desc, account, price, category])
    return sql_lines


_schwab_conversions = {
    "Amazon": lambda x: "Amazon Prime",
}