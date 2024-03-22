def schwab_to_sheets(output, lines, acc):
    converts_set = set(_schwab_conversions.keys())

    for line in reversed(lines):
        parts = list(filter(None, line.split("\t")))
        date = parts[0]
        desc = parts[2]
        price = parts[3]
        key = next((key for key in converts_set if key in desc), None)
        if key:
            desc = _schwab_conversions[key](desc)
        output.write(f"{date}@{desc}@{acc}@{price}\n")


_schwab_conversions = {
    "Amazon": lambda x: "Amazon Prime",
}