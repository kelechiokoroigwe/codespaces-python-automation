import json

file_path = "groceries_list.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)

print("apples quantity:", parsed_data["apples"])