from collections import Counter

sales_records = [
    {'product': 'Tablet', 'price': 600, 'quantity': 7},
    {'product': 'Laptop', 'price': 1200, 'quantity': 5},
    {'product': 'Phone', 'price': 800, 'quantity': 10},
    {'product': 'Tablet', 'price': 800, 'quantity': 1},
    {'product': 'Tablet', 'price': 800, 'quantity': 2},
    {'product': 'Laptop', 'price': 1100, 'quantity': 1},
]
def calculate_stats(data, field):
    values = [item[field] for item in data]
    return {
        'total': sum(values),
        'average': sum(values) / len(values),
        'maximum': max(values),
        'minimum': min(values),
        'count': len(values)
    }

price_stats = calculate_stats(sales_records, 'price')
print(price_stats)


product_counts = Counter(row['product'] for row in sales_records)
print(product_counts)

print (Counter([3,4,2,3,3,2,3,2,3,4,6,7,2]))


