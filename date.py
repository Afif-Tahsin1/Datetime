from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print(f"Today's date is: {today}")
print(f"\nCurrent date and time is {now}")
print(f"\nCurrent date components: {today.year} {today.month} {today.day}")