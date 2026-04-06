sales_records = [
    {'product': 'Tablet', 'price': 600, 'quantity': 7},
    {'product': 'Laptop', 'price': 1200, 'quantity': 5},
    {'product': 'Phone', 'price': 800, 'quantity': 10},
]
# print (sales_records[1] ['price'] )
# Find the price of Tablet

for row in sales_records:
    if row['product'] == 'Tablet':
        print (row['price'])

        
# In list comprehension 
# print ([row for row in sales_records if row['price'] > 600])

"""
for row in sales_records:
    if row['product'] == 'Tablet':
        print (row['price'])
"""
# print ([row for row in sales_records if row['price'] > 600])

sorted_by_price = sorted(sales_records, key=lambda x: x['quantity'])
print (sorted_by_price)

for row in sales_records:
    row ['product'] = row['quantity'] * row['price']


print(sales_records)