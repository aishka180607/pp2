from datetime import datetime, timedelta

current_data = datetime.now()
date_yesterday = current_data - timedelta(days = 1)
date_tomorrow = current_data + timedelta(days = 1)

print("The current data:", current_data)
print("Yesterday:", date_yesterday)
print("Tomorrow:", date_tomorrow)