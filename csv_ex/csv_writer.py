import csv
with open('csv_ex/sales_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([['tv','30', '50000', ]])
