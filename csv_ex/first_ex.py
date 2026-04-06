import csv

# Reading CSV file
with open('csv_ex/sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Get headers
    print ([row for row in reader])

    rows = []
    for row in reader:
        rows.append(row)
    print (rows)
