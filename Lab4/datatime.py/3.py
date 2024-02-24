import datetime
dt = datetime.datetime.today().replace(second=0)
print(dt)
#or
from datetime import datetime

current_data = datetime.now()
new_data = current_data.replace(microsecond = 0)

print(current_data)
print(new_data)
