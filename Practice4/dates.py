# dates.py

from datetime import datetime, timedelta, timezone

# current date and time
now = datetime.now()
print("Current datetime:", now)

# formatting date
formatted = now.strftime("%Y-%m-%d %H:%M")
print("Formatted:", formatted)

# add 7 days
future = now + timedelta(days=7)
print("After 7 days:", future)

# difference between dates
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 1, 10)

difference = date2 - date1
print("Difference in days:", difference.days)

# UTC timezone example
utc_time = datetime.now(timezone.utc)
print("UTC time:", utc_time)