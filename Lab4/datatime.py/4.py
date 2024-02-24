from datetime import datetime

current_data = datetime.now()
my_data = datetime(2024, 8, 11, 15, 1, 0)
difference_sec = (current_data - my_data).total_seconds()

print(difference_sec)