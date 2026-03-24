from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Today: {now.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")


import random
r = random.randint(1, 100)
print (r)
"""
random_numbers = [random.randint(1, 100) for _ in range(5)]
random_choice = random.choice(['apple', 'banana', 'orange'])
print(f"Random numbers: {random_numbers}")
print(f"Random fruit: {random_choice}")

"""
