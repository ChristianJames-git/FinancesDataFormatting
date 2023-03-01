filename = "desc.txt"

with open(filename, "r") as file:
    lines = file.readlines()

arrays = []
for line in lines:
    line = line.replace(" ", "_").strip("\n")  # removes spaces
    print(line)
