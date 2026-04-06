import csv

with open('csv_ex/sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['product'])
