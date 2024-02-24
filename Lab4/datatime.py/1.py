from datetime import datetime, timedelta
currentd = datetime.now()
newd = currentd - timedelta(days = 5)

print("The current date:", currentd)
print("Date after minus five days:", newd)
