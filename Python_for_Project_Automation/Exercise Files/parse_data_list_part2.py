import csv

file_path = "groceries_list.csv"
with open(file_path,"r") as file:
    csv_loader = csv.reader(file)
    headers = next(csv_loader)
    for row in csv_loader:
        row[1] = int(row[1])
        print(row)
























# import csv

# file_path = "groceries_list.csv"

# with open(file_path, "r") as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)
#     for row in csv_reader:
#         row[1] = int(row[1])
#         print(row)