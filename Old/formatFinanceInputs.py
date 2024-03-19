# fill in filename name of .txt to match the SQL table name
# file should be in order, excluding parentheses (date, description, quantity, account, category, {0 if not budget})
# returns SQL code

month = "22November"
filename = f"{month}.txt"  # Change this to your file's name

# Open the file and read its contents
with open(filename, "r") as file:
    lines = file.readlines()

# Split each line into an array based on spaces
# removes missed "," and "$"
arrays = []
for line in lines:
    line = line.replace(",", "").replace("$", "")
    array = line.split()
    arrays.append(array)

# format each line to the VALUES portion of an SQL statement
formatted_data = []
for item in arrays:
    formatted_item = f"'{item[0]}', '{item[1]}', '{item[4]}', '{item[3]}', {item[2]}"
    if len(item) == 6:
        formatted_item += f", {item[5]}"
    else:
        formatted_item += f", {1}"
    formatted_data.append(formatted_item)

# format and print SQL Insert statements
for data in formatted_data:
    query = f"INSERT INTO {month}(date, description, expense_type, account_id, quantity, budget) VALUES ({data});"
    print(query)
